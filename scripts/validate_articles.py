#!/usr/bin/env python3
"""
Fluente-Mente Article Writer QA
Checks structural integrity of generated Markdown drafts.
It deliberately fails on unresolved placeholders so human/LLM writing cannot
accidentally pass as publish-ready.
"""
from pathlib import Path
import argparse, re, yaml

REQUIRED = [
    "content_id","title","slug","description","domain","cluster","topic",
    "content_type","level","skill","user_job","learning_outcome",
    "search_intent","primary_keyword","funnel_role","commercial_intent",
    "primary_cta","status"
]

PLACEHOLDER_PATTERNS = [
    r"\[MODEL SENTENCE FROM LEARNING BRIEF\]",
    r"\[TEXTBOOK / LITERAL VERSION\]",
    r"\[NATURAL VERSION\]",
    r"\[CTA_PRIMARY\]",
    r"CONFIGURE"
]

def parse_md(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    fm = yaml.safe_load(text[4:end]) or {}
    body = text[end+4:]
    return fm, body

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--drafts", default="_articles/drafts")
    ap.add_argument("--fail-on-placeholder", action="store_true")
    args = ap.parse_args()

    root = Path(args.root)
    files = sorted((root/args.drafts).glob("article-*.md"))
    errors=[]
    checked=0

    for p in files:
        checked += 1
        fm, body = parse_md(p)
        if fm is None:
            errors.append(f"{p.name}: invalid or missing YAML front matter")
            continue
        missing=[k for k in REQUIRED if fm.get(k) in (None,"")]
        if missing:
            errors.append(f"{p.name}: missing fields: {', '.join(missing)}")
        if fm.get("status") != "drafting":
            errors.append(f"{p.name}: status must remain drafting")
        if body.count("\n# ") != 1:
            errors.append(f"{p.name}: expected exactly one H1")
        if args.fail_on_placeholder:
            for pat in PLACEHOLDER_PATTERNS:
                if re.search(pat, p.read_text(encoding="utf-8")):
                    errors.append(f"{p.name}: unresolved placeholder matched {pat}")

    report={"checked":checked,"errors":errors,"status":"ok" if not errors else "failed"}
    out=root/"_articles"/"qa"/"WRITER_QA_REPORT.yml"
    out.write_text(yaml.safe_dump(report,allow_unicode=True,sort_keys=False),encoding="utf-8")
    print(yaml.safe_dump(report,allow_unicode=True,sort_keys=False))
    raise SystemExit(0 if not errors else 1)

if __name__=="__main__":
    main()
