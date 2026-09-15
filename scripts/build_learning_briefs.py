#!/usr/bin/env python3
"""Generate learning-brief YAML records from _data/content.yml.

The engine intentionally does not invent language content. It carries canonical
metadata forward and creates explicit author/AI slots for pedagogical design.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def brief_for(item: dict) -> dict:
    focus = item.get("primary_language_focus") or item.get("skill")
    return {
        "schema_version": "1.0",
        "brief_id": f"BRIEF-{item['content_id']}",
        "status": "generated_pending_learning_design",
        "source": {
            "source_file": "_data/content.yml",
            "content_id": item["content_id"],
            "content_schema_version": "2.0",
        },
        "identity": {
            "title": item.get("title"),
            "slug": item.get("slug"),
            "content_type": item.get("content_type"),
            "level": item.get("level"),
            "domain": item.get("domain"),
            "cluster": item.get("cluster"),
            "topic": item.get("topic"),
        },
        "learner": {
            "user_job": item.get("user_job"),
            "communicative_goal": item.get("user_job"),
            "learner_outcome": item.get("learning_outcome"),
            "primary_skill": item.get("skill"),
        },
        "language_goal": {
            "primary_language_focus": focus,
            "target_expressions": item.get("target_expressions") or {"core": [], "supporting": []},
            "target_words": item.get("target_words") or {"core": [], "supporting": []},
            "grammar_focus": as_list(item.get("grammar_focus")),
            "natural_english": bool(item.get("natural_english")),
            "textbook_vs_natural": bool(item.get("textbook_vs_natural")),
        },
        "model_sentences": [],
        "dialogue_design": {
            "required": item.get("content_type") in {"RLG", "QA"},
            "situation": None,
            "speakers": [],
            "turn_count_target": None,
            "must_include_core_expressions": True,
            "notes": "DESIGN_REQUIRED",
        },
        "story_design": {
            "required": item.get("content_type") == "RLG",
            "scenario": None,
            "purpose": None,
            "notes": "DESIGN_REQUIRED",
        },
        "textbook_vs_natural": {
            "enabled": bool(item.get("textbook_vs_natural")),
            "textbook_example": None,
            "natural_example": None,
            "why_it_matters": None,
        },
        "practice": {
            "controlled": [],
            "guided": [],
            "transfer": [],
            "self_check": [],
        },
        "progression": {
            "previous_content": item.get("parent_content"),
            "related_content": item.get("related_content") or [],
            "next_content": item.get("recommended_next_content") or [],
            "learning_paths": item.get("learning_path") or [],
        },
        "funnel": {
            "funnel_role": item.get("funnel_role"),
            "commercial_intent": item.get("commercial_intent"),
            "babbel_relevance": item.get("babbel_relevance"),
            "primary_cta": item.get("primary_cta"),
        },
        "seo": {
            "primary_keyword": item.get("primary_keyword"),
            "secondary_keywords": item.get("secondary_keywords") or [],
            "search_intent": item.get("search_intent"),
        },
        "pinterest": {
            "intent": item.get("pinterest_intent"),
            "angle": item.get("pinterest_angle"),
            "pin_count": item.get("pin_count"),
        },
        "qa": {
            "one_primary_learning_outcome": True,
            "core_language_is_reused": True,
            "examples_are_contextual": None,
            "difficulty_matches_level": None,
            "no_unsupported_claims": True,
            "no_duplicative_primary_intent": None,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    src = root / "_data" / "content.yml"
    out_dir = root / "_data" / "learning_briefs"
    out_dir.mkdir(parents=True, exist_ok=True)

    data = load_yaml(src)
    items = data.get("content", [])
    if not isinstance(items, list):
        raise SystemExit("content.yml: 'content' must be a list")

    manifest = {"schema_version": "1.0", "generated_from": "_data/content.yml", "count": len(items), "briefs": []}
    for item in items:
        brief = brief_for(item)
        cid = item["content_id"]
        target = out_dir / f"{cid}.yml"
        with target.open("w", encoding="utf-8") as f:
            yaml.safe_dump(brief, f, allow_unicode=True, sort_keys=False, width=120)
        manifest["briefs"].append({"content_id": cid, "brief_file": f"_data/learning_briefs/{cid}.yml"})

    manifest_path = Path(args.output).resolve() if args.output else root / "_data" / "learning_briefs.yml"
    with manifest_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(manifest, f, allow_unicode=True, sort_keys=False, width=120)
    print(f"Generated {len(items)} learning briefs in {out_dir}")
    print(f"Manifest: {manifest_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
