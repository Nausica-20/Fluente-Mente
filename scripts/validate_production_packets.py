#!/usr/bin/env python3
"""
Fluente-Mente Article QA Gate.
Validates generated production packets before prose can be accepted.
"""
from pathlib import Path
import argparse, yaml

REQUIRED_FM = [
    "content_id","title","slug","description","domain","cluster","topic",
    "content_type","level","skill","user_job","learning_outcome",
    "search_intent","primary_keyword","funnel_role","commercial_intent",
    "primary_cta","status"
]

def read_yaml(p):
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--packets", default="_articles/generated")
    args=ap.parse_args()
    root=Path(args.root)
    files=sorted((root/args.packets).glob("*.yml"))
    files=[p for p in files if p.name!="PRODUCTION_REPORT.yml"]
    errors=[]
    checked=0
    for p in files:
        d=read_yaml(p)
        checked+=1
        if d.get("status") != "production_ready":
            errors.append(f"{p.name}: packet not production_ready")
        fm=d.get("front_matter_contract",{})
        missing=[k for k in REQUIRED_FM if fm.get(k) in (None,"")]
        if missing:
            errors.append(f"{p.name}: missing front matter fields: {', '.join(missing)}")
        qa=d.get("qa_gate",{})
        if qa.get("publish_decision") != "PENDING_QA":
            errors.append(f"{p.name}: publish decision must be PENDING_QA")
    report={"checked":checked,"errors":errors,"status":"ok" if not errors else "failed"}
    out=root/"_articles"/"qa"/"PRODUCTION_QA_REPORT.yml"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(report,allow_unicode=True,sort_keys=False),encoding="utf-8")
    print(yaml.safe_dump(report,allow_unicode=True,sort_keys=False))
    raise SystemExit(0 if not errors else 1)

if __name__=="__main__":
    main()
