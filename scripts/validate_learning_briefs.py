#!/usr/bin/env python3
from __future__ import annotations
import argparse, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load(p):
    with open(p, encoding="utf-8") as f: return yaml.safe_load(f)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root', default=str(ROOT)); args=ap.parse_args()
    root=Path(args.root).resolve(); data=load(root/'_data/content.yml')
    content={x['content_id']:x for x in data.get('content',[])}
    d=root/'_data'/'learning_briefs'
    errs=[]; seen=[]
    for p in sorted(d.glob('*.yml')):
        if p.name=='manifest.yml': continue
        b=load(p); seen.append(p.stem)
        if not b: errs.append(f'{p.name}: empty') ; continue
        cid=b.get('source',{}).get('content_id')
        if cid not in content: errs.append(f'{p.name}: unknown content_id {cid}'); continue
        c=content[cid]
        checks=[
            ('brief_id', f"BRIEF-{cid}"),
            ('schema_version','1.0'),
        ]
        for k,v in checks:
            if b.get(k)!=v: errs.append(f'{p.name}: {k} != {v}')
        pairs=[
            ('identity','content_type','content_type'),('identity','domain','domain'),('identity','cluster','cluster'),('identity','topic','topic'),('identity','level','level'),
            ('learner','learner_outcome','learning_outcome'),('seo','primary_keyword','primary_keyword'),('seo','search_intent','search_intent'),
            ('funnel','primary_cta','primary_cta'),('funnel','funnel_role','funnel_role'),('funnel','commercial_intent','commercial_intent'),
            ('pinterest','intent','pinterest_intent'),('pinterest','angle','pinterest_angle')]
        for section,bk,ck in pairs:
            if b.get(section,{}).get(bk)!=c.get(ck): errs.append(f'{p.name}: {section}.{bk} mismatch')
        pg=b.get('language_goal',{}); ce=pg.get('target_expressions',{}) or {}; cw=pg.get('target_words',{}) or {}
        if len(ce.get('core',[]) or [])>8: errs.append(f'{p.name}: too many core expressions')
        if len(ce.get('supporting',[]) or [])>12: errs.append(f'{p.name}: too many supporting expressions')
        if len(cw.get('core',[]) or [])>8: errs.append(f'{p.name}: too many core words')
        if len(cw.get('supporting',[]) or [])>12: errs.append(f'{p.name}: too many supporting words')
        if not isinstance(b.get('model_sentences'), list): errs.append(f'{p.name}: model_sentences must be list')
        for key in ['controlled','guided','transfer','self_check']:
            if not isinstance(b.get('practice',{}).get(key), list): errs.append(f'{p.name}: practice.{key} must be list')
    missing=sorted(set(content)-set(seen))
    if missing: errs.append('missing briefs: '+', '.join(missing))
    print(f'Learning briefs checked: {len(seen)}')
    if errs:
        print(f'ERRORS: {len(errs)}')
        for e in errs: print(' -',e)
        return 1
    print('ERRORS: 0')
    return 0
if __name__=='__main__': sys.exit(main())
