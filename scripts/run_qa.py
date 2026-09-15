#!/usr/bin/env python3
"""
Fluente-Mente QA Engine v1.0

Audits article drafts against canonical data and quality gates.

Decision model:
- PASS: no blocking issues and no review flags
- REVIEW: no blocking issues, but one or more editorial/language checks need review
- FAIL: one or more blocking issues

This engine deliberately does NOT pretend to validate native-level English
semantics with regex. It identifies structural and data integrity issues and
creates a review queue for human/LLM linguistic judgment.
"""

from pathlib import Path
import argparse, re, yaml, json

SECTIONS = [
    "front_matter",
    "architecture",
    "learning_design",
    "language",
    "seo",
    "internal_linking",
    "funnel",
    "pinterest",
    "editorial"
]

BLOCKING_FRONT_MATTER = [
    "content_id","title","slug","description","domain","cluster","topic",
    "content_type","level","skill","user_job","learning_outcome",
    "search_intent","primary_keyword","funnel_role",
    "commercial_intent","primary_cta","status"
]

def load_yaml(p):
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def parse_md(p):
    text = p.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    try:
        fm = yaml.safe_load(text[4:end]) or {}
    except Exception:
        return "YAML_ERROR", text
    body = text[end+4:]
    return fm, body

def ids_from_doc(doc, key_candidates):
    for k in key_candidates:
        v = doc.get(k)
        if isinstance(v, list):
            return {x.get("content_id") for x in v if isinstance(x, dict) and x.get("content_id")}
    return set()

def normalize_items(doc, *keys):
    for k in keys:
        if isinstance(doc.get(k), list):
            return doc[k]
    return []

def add(checks, section, rule, status, message, evidence=""):
    checks.append({
        "section": section,
        "rule": rule,
        "status": status,
        "message": message,
        "evidence": evidence[:300]
    })

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--drafts", default="_articles/drafts")
    ap.add_argument("--content", default="_data/content.yml")
    ap.add_argument("--briefs", default="_data/learning_briefs.yml")
    ap.add_argument("--report", default="_articles/qa/QA_REPORT.yml")
    ap.add_argument("--review-queue", default="_articles/qa/REVIEW_QUEUE.yml")
    ap.add_argument("--fail-on-review", action="store_true")
    args = ap.parse_args()

    root = Path(args.root)
    content_doc = load_yaml(root/args.content)
    brief_doc = load_yaml(root/args.briefs)

    content_items = normalize_items(content_doc, "contents", "content", "items")
    brief_items = normalize_items(brief_doc, "briefs", "learning_briefs", "items")
    cidx = {x.get("content_id"): x for x in content_items if isinstance(x, dict) and x.get("content_id")}
    bidx = {x.get("content_id"): x for x in brief_items if isinstance(x, dict) and x.get("content_id")}

    drafts = sorted((root/args.drafts).glob("article-*.md"))
    reports = []
    review_queue = []
    total_fail = total_review = total_pass = 0

    for p in drafts:
        fm, body = parse_md(p)
        checks = []
        cid = None
        if fm == "YAML_ERROR" or fm is None:
            add(checks, "front_matter", "parse_yaml", "FAIL", "Front matter YAML non valido.")
        else:
            cid = fm.get("content_id")
            missing = [k for k in BLOCKING_FRONT_MATTER if fm.get(k) in (None, "")]
            if missing:
                add(checks, "front_matter", "required_fields", "FAIL", f"Campi mancanti: {', '.join(missing)}")
            if fm.get("status") not in ("drafting", "qa", "published"):
                add(checks, "front_matter", "valid_status", "FAIL", f"Status non valido: {fm.get('status')}")
            if fm.get("index") is False and fm.get("status") == "published":
                add(checks, "seo", "published_indexable", "FAIL", "Un articolo pubblicato non può essere noindex senza una regola esplicita.")
            if cid not in cidx:
                add(checks, "architecture", "canonical_content_id", "FAIL", f"content_id {cid} non presente in content.yml.")
            else:
                canonical = cidx[cid]
                for k in ["domain","cluster","topic","content_type","level","funnel_role","commercial_intent","primary_cta"]:
                    if fm.get(k) != canonical.get(k):
                        add(checks, "architecture", f"match_{k}", "FAIL",
                            f"{k}: front matter={fm.get(k)!r}, content.yml={canonical.get(k)!r}")
                if fm.get("primary_keyword") != canonical.get("primary_keyword"):
                    add(checks, "seo", "primary_keyword_sync", "FAIL",
                        "primary_keyword non sincronizzata con content.yml.")
                if fm.get("slug") != canonical.get("slug"):
                    add(checks, "architecture", "slug_sync", "FAIL",
                        "slug non sincronizzato con content.yml.")
            brief = bidx.get(cid)
            if not brief:
                add(checks, "learning_design", "brief_exists", "FAIL", f"Learning Brief mancante per {cid}.")
            else:
                if brief.get("content_id") != cid:
                    add(checks, "learning_design", "brief_id", "FAIL", "ID del brief non coerente.")
                # Core language presence in text is a deterministic proxy, not a semantic validation.
                lt = brief.get("language_targets", {}) or {}
                ex = (lt.get("expressions") or lt.get("target_expressions") or {})
                wd = (lt.get("words") or lt.get("target_words") or {})
                core_expr = ex.get("core", []) if isinstance(ex, dict) else []
                core_words = wd.get("core", []) if isinstance(wd, dict) else []
                body_low = body.lower()
                missing_core_expr = [x for x in core_expr if str(x).lower() not in body_low]
                if missing_core_expr:
                    add(checks, "learning_design", "core_expressions_used", "REVIEW",
                        "Core expressions non rilevate letteralmente nel draft.", ", ".join(map(str, missing_core_expr)))
                missing_core_words = [x for x in core_words if str(x).lower() not in body_low]
                if missing_core_words:
                    add(checks, "learning_design", "core_words_used", "REVIEW",
                        "Core words non rilevate letteralmente nel draft.", ", ".join(map(str, missing_core_words)))
                if brief.get("content", {}).get("communicative_goal") and \
                   str(brief["content"]["communicative_goal"]).lower() not in body_low:
                    add(checks, "learning_design", "goal_alignment_semantic", "REVIEW",
                        "La presenza dell'obiettivo non può essere verificata con certezza dal motore; revisione editoriale richiesta.")
            # Structure checks
            h1 = re.findall(r"(?m)^#\s+(.+)$", body)
            if len(h1) != 1:
                add(checks, "editorial", "single_h1", "FAIL", f"Attesi 1 H1, trovati {len(h1)}.")
            if len(body.strip()) < 1200:
                add(checks, "editorial", "minimum_body_length", "REVIEW", "Draft molto breve: verificare profondità e utilità.")
            if re.search(r"\[(?:MODEL|TEXTBOOK|NATURAL|CTA|INSERT|TODO)[^\]]*\]", body, re.I):
                add(checks, "editorial", "no_placeholders", "FAIL", "Placeholder irrisolti presenti nel draft.")
            # English sanity flags: review, not automated correctness
            english_blocks = re.findall(r">?\s*[*_`]*([A-Za-z][A-Za-z' -]{2,})[*_`]*", body)
            if not english_blocks:
                add(checks, "language", "english_examples_present", "REVIEW", "Nessun esempio inglese riconoscibile: verificare il contenuto didattico.")
            # SEO
            if fm.get("meta_title") and len(str(fm["meta_title"])) > 70:
                add(checks, "seo", "meta_title_length", "REVIEW", "Meta title potenzialmente troppo lungo.")
            if fm.get("meta_description") and len(str(fm["meta_description"])) > 170:
                add(checks, "seo", "meta_description_length", "REVIEW", "Meta description potenzialmente troppo lunga.")
            if fm.get("primary_keyword"):
                pk = str(fm["primary_keyword"]).lower()
                if pk not in str(fm.get("title","")).lower() and pk not in body.lower():
                    add(checks, "seo", "keyword_presence", "REVIEW", "Primary keyword non rilevata in titolo o corpo.")
            # Internal link target existence
            if cid in cidx:
                rel = fm.get("related_content") or []
                if isinstance(rel, str): rel = [rel]
                missing_rel = [x for x in rel if x not in cidx]
                if missing_rel:
                    add(checks, "internal_linking", "related_ids_exist", "FAIL",
                        "Related content ID inesistenti.", ", ".join(missing_rel))
            # Funnel / Babbel
            if fm.get("commercial_intent") == "none" and "Babbel" in body:
                add(checks, "funnel", "commercial_boundary", "REVIEW",
                    "Contenuto non commerciale ma menziona Babbel: verificare che il riferimento sia realmente contestuale.")
            # Pinterest
            if fm.get("pinterest_intent") in (None, ""):
                add(checks, "pinterest", "intent_present", "REVIEW", "Pinterest intent assente.")
            # State logic
            fails = [c for c in checks if c["status"] == "FAIL"]
            reviews = [c for c in checks if c["status"] == "REVIEW"]
            if fails:
                decision = "FAIL"; total_fail += 1
            elif reviews:
                decision = "REVIEW"; total_review += 1
            else:
                decision = "PASS"; total_pass += 1

            reports.append({
                "file": str(p.relative_to(root)),
                "content_id": cid,
                "decision": decision,
                "checks": checks
            })
            if decision in ("FAIL","REVIEW"):
                review_queue.append({
                    "content_id": cid,
                    "file": str(p.relative_to(root)),
                    "decision": decision,
                    "review_items": [c for c in checks if c["status"] != "PASS"]
                })
            continue

        reports.append({
            "file": str(p.relative_to(root)),
            "content_id": cid,
            "decision": "FAIL",
            "checks": checks
        })
        total_fail += 1
        review_queue.append({
            "content_id": cid,
            "file": str(p.relative_to(root)),
            "decision": "FAIL",
            "review_items": checks
        })

    result = {
        "schema_version": "1.0",
        "engine": "fluente-mente-qa",
        "summary": {
            "articles_checked": len(reports),
            "pass": total_pass,
            "review": total_review,
            "fail": total_fail
        },
        "reports": reports
    }
    rp = root/args.report
    rp.parent.mkdir(parents=True, exist_ok=True)
    rp.write_text(yaml.safe_dump(result, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")

    rq = root/args.review_queue
    rq.parent.mkdir(parents=True, exist_ok=True)
    rq.write_text(yaml.safe_dump({
        "schema_version": "1.0",
        "review_count": len(review_queue),
        "items": review_queue
    }, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")

    print(yaml.safe_dump(result["summary"], allow_unicode=True, sort_keys=False))
    if total_fail or (args.fail_on_review and total_review):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
