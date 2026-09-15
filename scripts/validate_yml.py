#!/usr/bin/env python3
"""Validate the Fluente-Mente YAML contract and article front matter."""
from pathlib import Path
import argparse, re, sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data"
SCHEMA = ROOT / "schemas" / "article.schema.yml"
DIDACTIC = {"QA", "RLG", "LES", "PS", "REF"}

def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))

def parse_front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
    if not m:
        raise ValueError("front matter YAML non trovato o delimitatori --- mancanti")
    data = yaml.safe_load(m.group(1))
    if not isinstance(data, dict):
        raise ValueError("front matter deve essere una mappa YAML")
    return data

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--articles", default="_articles")
    ap.add_argument("--strict", action="store_true", help="trasforma anche i warning cross-file in errori")
    args = ap.parse_args()
    root = Path(args.root)
    data = root / "_data"
    schema = load(root / "schemas" / "article.schema.yml")
    files = {n: load(data / n) for n in ["content.yml","clusters.yml","topics.yml","learning_paths.yml","ctas.yml","pinterest.yml"]}
    errors, warnings = [], []
    content = files["content.yml"]["content"]
    clusters = files["clusters.yml"]["domains"]
    topics = {x["topic_id"]: x for x in files["topics.yml"]["topics"]}
    paths = {x["path_id"] for x in files["learning_paths.yml"]["learning_paths"]}
    ctas = {x["cta_id"] for x in files["ctas.yml"]["ctas"]}
    pinmap = files["pinterest.yml"]["content_mapping"]
    domain_clusters = {d: set(v.get("clusters", {}).keys()) for d,v in clusters.items()}
    content_ids = {r.get("content_id") for r in content}

    def problem(msg, strict_cross=False):
        if strict_cross and not args.strict:
            warnings.append(msg)
        else:
            errors.append(msg)

    slugs, canonicals = set(), set()
    for i, r in enumerate(content, 1):
        label = f"content #{i} ({r.get('content_id','?')})"
        for k in schema["modes"]["content_registry"]["required"]:
            if k not in r:
                errors.append(f"{label}: campo obbligatorio mancante: {k}")
        cid = r.get("content_id")
        if cid in content_ids and sum(x.get("content_id") == cid for x in content) > 1:
            errors.append(f"{label}: content_id duplicato: {cid}")
        slug = r.get("slug")
        if not isinstance(slug, str) or not re.fullmatch(schema["production"]["slug_pattern"], slug):
            errors.append(f"{label}: slug non valido: {slug!r}")
        elif slug in slugs:
            errors.append(f"{label}: slug duplicato: {slug}")
        slugs.add(slug)
        canonical = r.get("canonical")
        if canonical:
            if not canonical.endswith("/"): errors.append(f"{label}: canonical deve terminare con /")
            if canonical in canonicals: errors.append(f"{label}: canonical duplicata: {canonical}")
            canonicals.add(canonical)
        for k in ["related_content","learning_path","secondary_keywords","grammar_focus","recommended_next_content"]:
            if not isinstance(r.get(k), list): errors.append(f"{label}: {k} deve essere una lista")
        for k, allowed in schema["enums"].items():
            if r.get(k) not in allowed: errors.append(f"{label}: {k} non valido: {r.get(k)!r}")
        for b in schema["types"]["boolean_fields"]:
            if not isinstance(r.get(b), bool): errors.append(f"{label}: {b} deve essere boolean")
        if not isinstance(r.get("pin_count"), int) or r["pin_count"] < 0: errors.append(f"{label}: pin_count deve essere intero >= 0")
        for key in ["target_expressions","target_words"]:
            obj=r.get(key)
            if not isinstance(obj,dict) or not all(isinstance(obj.get(x),list) for x in ["core","supporting"]):
                errors.append(f"{label}: {key} deve contenere core e supporting come liste")
        domain, cluster = r.get("domain"), r.get("cluster")
        if domain not in domain_clusters: errors.append(f"{label}: domain sconosciuto: {domain}")
        elif cluster not in domain_clusters[domain]: errors.append(f"{label}: cluster {cluster!r} non appartiene a {domain!r}")
        t=topics.get(r.get("topic"))
        if not t: errors.append(f"{label}: topic sconosciuto: {r.get('topic')}")
        else:
            if t.get("domain") != domain: problem(f"{label}: topic/domain mismatch", True)
            if t.get("cluster") != cluster: problem(f"{label}: topic/cluster mismatch", True)
            if cid not in t.get("content_ids",[]): problem(f"{label}: topic {r.get('topic')} non elenca {cid}", True)
        for ref in r.get("related_content",[]) + r.get("recommended_next_content",[]):
            if ref not in content_ids: errors.append(f"{label}: riferimento contenuto inesistente: {ref}")
        if r.get("parent_content") and r["parent_content"] not in content_ids: errors.append(f"{label}: parent_content inesistente: {r['parent_content']}")
        for ref in r.get("learning_path",[]):
            if ref not in paths: errors.append(f"{label}: learning_path inesistente: {ref}")
        if r.get("recommended_path") and r["recommended_path"] not in paths: errors.append(f"{label}: recommended_path inesistente: {r['recommended_path']}")
        if r.get("primary_cta") not in ctas: errors.append(f"{label}: primary_cta inesistente: {r.get('primary_cta')}")
        if cid not in pinmap: errors.append(f"{label}: mapping Pinterest mancante")
        else:
            mapped=pinmap[cid]
            if r.get("pinterest_intent") != mapped.get("primary_intent"):
                problem(f"{label}: pinterest_intent differisce dal mapping", True)

    article_dir=root/args.articles
    article_files=sorted(article_dir.glob("article-*.md")) if article_dir.exists() else []
    for f in article_files:
        try:
            r=parse_front_matter(f)
        except Exception as e:
            errors.append(f"{f}: {e}"); continue
        for k in schema["modes"]["article_front_matter"]["required"]:
            if k not in r: errors.append(f"{f}: campo obbligatorio mancante: {k}")
        if r.get("content_type") in DIDACTIC:
            for k in ["target_expressions","target_words"]:
                if not r.get(k): errors.append(f"{f}: {k} obbligatorio per {r.get('content_type')}")
        if r.get("content_id") not in content_ids: errors.append(f"{f}: content_id non presente in content.yml: {r.get('content_id')}")

    if errors:
        print(f"VALIDATION FAILED: {len(errors)} errori, {len(warnings)} warning")
        for x in errors: print("ERROR:",x)
        for x in warnings: print("WARNING:",x)
        return 1
    print(f"VALIDATION PASSED: {len(content)} record content, {len(article_files)} articoli, {len(warnings)} warning")
    for x in warnings: print("WARNING:",x)
    return 0

if __name__ == "__main__": sys.exit(main())
