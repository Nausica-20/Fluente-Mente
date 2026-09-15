#!/usr/bin/env python3
from pathlib import Path
import argparse, yaml

REQUIRED_CONTENT = [
    'content_id','title','slug','description','domain','cluster','topic',
    'content_type','level','skill','user_job','learning_outcome',
    'search_intent','primary_keyword','funnel_role','commercial_intent',
    'primary_cta','status'
]
REQUIRED_BRIEF = ['schema_version','brief_id','status','source','identity','learner','language_goal','funnel','seo','pinterest','qa']

def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding='utf-8')) or {}

def items_from_content(doc):
    return doc.get('contents', doc.get('content', doc.get('items', [])))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',default='.')
    ap.add_argument('--content',default='_data/content.yml')
    ap.add_argument('--briefs-index',default='_data/learning_briefs.yml')
    ap.add_argument('--brief-dir',default='_data/learning_briefs')
    ap.add_argument('--out',default='_articles/generated')
    args=ap.parse_args()
    root=Path(args.root)
    content=load_yaml(root/args.content)
    brief_index=load_yaml(root/args.briefs_index)
    citems=items_from_content(content)
    cidx={x['content_id']:x for x in citems if isinstance(x,dict) and 'content_id' in x}
    bmeta={x['content_id']:x for x in brief_index.get('briefs',[]) if isinstance(x,dict) and 'content_id' in x}
    out=root/args.out; out.mkdir(parents=True,exist_ok=True)
    errors=[]; created=0
    for cid,item in sorted(cidx.items()):
        missing=[k for k in REQUIRED_CONTENT if item.get(k) in (None,'')]
        if missing:
            errors.append(f'{cid}: content missing {", ".join(missing)}'); continue
        meta=bmeta.get(cid)
        if not meta:
            errors.append(f'{cid}: missing brief index entry'); continue
        rel=meta.get('brief_file')
        if not rel:
            errors.append(f'{cid}: brief_file missing'); continue
        bp=root/rel
        if not bp.exists():
            errors.append(f'{cid}: brief file not found: {rel}'); continue
        brief=load_yaml(bp)
        miss=[k for k in REQUIRED_BRIEF if k not in brief]
        if miss:
            errors.append(f'{cid}: brief missing {", ".join(miss)}'); continue
        if brief.get('source',{}).get('content_id') != cid:
            errors.append(f'{cid}: brief source.content_id mismatch'); continue
        fm={
            'content_id':cid,'title':item.get('title'),'slug':item.get('slug'),
            'description':item.get('description'),'date':'CONFIGURE','last_modified':'CONFIGURE',
            'author':'Fluente-Mente','language':'it','domain':item.get('domain'),
            'cluster':item.get('cluster'),'topic':item.get('topic'),'content_type':item.get('content_type'),
            'level':item.get('level'),'skill':item.get('skill'),'user_job':item.get('user_job'),
            'learning_outcome':item.get('learning_outcome'),'search_intent':item.get('search_intent'),
            'primary_keyword':item.get('primary_keyword'),'secondary_keywords':item.get('secondary_keywords',[]),
            'canonical':item.get('canonical'),'meta_title':item.get('meta_title'),'meta_description':item.get('meta_description'),
            'funnel_role':item.get('funnel_role'),'commercial_intent':item.get('commercial_intent'),
            'primary_cta':item.get('primary_cta'),'status':'drafting','evergreen':item.get('evergreen',True),
            'index':item.get('index',True),'follow':item.get('follow',True),'sitemap':item.get('sitemap',True)
        }
        packet={
            'schema_version':'1.1','content_id':cid,'status':'production_ready',
            'source':{'content_registry':args.content,'learning_brief_index':args.briefs_index,'learning_brief_file':rel},
            'front_matter_contract':fm,
            'article_blueprint':{
                'learning_brief':brief,
                'required_principles':[
                    'Write the article in Italian.',
                    'English examples must be natural and context-appropriate.',
                    'Respect level, skill, user_job and learner_outcome.',
                    'Use only language targets explicitly designed in the learning brief.',
                    'Keep tone adult, clear, practical and non-school-like.',
                    'Do not invent Babbel offers, pricing, claims or results.',
                    'Do not publish automatically; QA approval is required.'
                ]
            },
            'qa_gate':{
                'required':True,
                'publish_decision':'PENDING_QA',
                'checks':['front_matter_schema','brief_alignment','english_accuracy','naturalness','level_fit','seo','internal_links','cta','affiliate_disclosure']
            }
        }
        (out/f'{cid}.yml').write_text(yaml.safe_dump(packet,allow_unicode=True,sort_keys=False,width=120),encoding='utf-8')
        created+=1
    report={'created':created,'expected':len(cidx),'errors':errors,'status':'ok' if not errors and created==len(cidx) else 'failed'}
    (out/'PRODUCTION_REPORT.yml').write_text(yaml.safe_dump(report,allow_unicode=True,sort_keys=False),encoding='utf-8')
    print(yaml.safe_dump(report,allow_unicode=True,sort_keys=False))
    raise SystemExit(0 if report['status']=='ok' else 1)
if __name__=='__main__': main()
