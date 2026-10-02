#!/usr/bin/env python3
from pathlib import Path
import argparse, sys, yaml

def load(p):
    with p.open(encoding='utf-8') as f: return yaml.safe_load(f) or {}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); args=ap.parse_args(); root=Path(args.root)
    reg=load(root/'_data/content_registry.yml'); errors=[]
    entries=reg.get('entries',[])
    if len(entries)!=841: errors.append(f'Expected 841 registry entries, found {len(entries)}')
    ids=[e.get('id') for e in entries]; urls=[e.get('url') for e in entries]; slugs=[e.get('slug') for e in entries]
    for label,vals in [('id',ids),('url',urls),('slug',slugs)]:
        dup=sorted({x for x in vals if vals.count(x)>1});
        if dup: errors.append(f'Duplicate {label}: {dup[:10]}')
    for e in entries:
        u=e.get('url','').strip('/')
        if not u: errors.append(f"{e.get('id')}: empty url"); continue
        p=root/u/'index.md'
        if not p.exists(): errors.append(f"{e.get('id')}: missing physical page {p}")
        elif not p.read_text(encoding='utf-8').startswith('---\n'): errors.append(f"{e.get('id')}: missing front matter")
    counts={}
    for e in entries: counts[e.get('content_type')]=counts.get(e.get('content_type'),0)+1
    expected={'daily_pill':365,'situation_article':52,'grammar_article':52,'confusion_article':259,'travel_article':26,'business_article':26,'culture_article':24,'adult_learning_article':24,'babbel_page':7,'pills_index':1,'situations_index':1,'grammar_index':1,'expressions_index':1,'words_index':1,'confusions_index':1}
    for k,v in expected.items():
        if counts.get(k,0)!=v: errors.append(f'{k}: expected {v}, found {counts.get(k,0)}')
    for rel in ['_config.yml','_data/site.yml','_data/content_registry.yml','_data/master_content_architecture.yml']:
        if not (root/rel).exists(): errors.append(f'Missing required file {rel}')
    if errors:
        print(f'VALIDATION FAILED: {len(errors)} errors')
        for e in errors: print('ERROR:',e)
        return 1
    print('VALIDATION PASSED: 841 registry records, 841 physical record routes, unique IDs/slugs/URLs')
    return 0
if __name__=='__main__': sys.exit(main())
