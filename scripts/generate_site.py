#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path
import yaml

def slugify(value: str) -> str:
    value = (value or '').strip().lower()
    value = re.sub(r'[^\w\s-]', '', value, flags=re.UNICODE)
    return re.sub(r'[-\s]+', '-', value).strip('-')

def load(path: Path):
    with path.open(encoding='utf-8') as f:
        return yaml.safe_load(f) or {}

def write_page(path: Path, front: dict, body: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = '---\n' + yaml.safe_dump(front, allow_unicode=True, sort_keys=False).rstrip() + '\n---\n\n' + body.rstrip() + '\n'
    path.write_text(text, encoding='utf-8')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    args = ap.parse_args()
    root = Path(args.root).resolve(); data = root/'_data'; out = root/'_generated'; out.mkdir(exist_ok=True)
    site = load(data/'site.yml'); content_db = load(data/'content.yml'); clusters_db = load(data/'clusters.yml'); topics_db = load(data/'topics.yml'); paths_db = load(data/'learning_paths.yml')
    contents = content_db.get('content', []); by_id = {x.get('content_id'): x for x in contents}
    for key, section in site.get('content_sections', {}).items():
        domain = section.get('domain')
        body = f"# {section.get('label', key)}\n\n{section.get('mission','')}\n\n"
        body += "{% assign items = site.data.content.content | where: 'domain', '" + str(domain) + "' %}\n"
        body += "{% for item in items %}\n### {{ item.title | default: item.user_job }}\n{{ item.learning_outcome }}\n\n{% endfor %}"
        write_page(out/f'{key}.md', {'layout':'hub','title':section.get('label', key),'description':section.get('mission',''),'permalink':section.get('url', f'/{key}/'),'domain':domain}, body)
    raw_domains = clusters_db.get('domains', {})
    domains = [{'domain_id': k, **(v or {})} for k, v in raw_domains.items()] if isinstance(raw_domains, dict) else raw_domains
    for domain in domains:
        domain_id = domain.get('domain_id') or domain.get('id') or domain.get('domain')
        raw_clusters = domain.get('clusters', {})
        clusters = [{'cluster_id': k, **(v or {})} for k, v in raw_clusters.items()] if isinstance(raw_clusters, dict) else raw_clusters
        for cluster in clusters:
            cid = cluster.get('cluster_id') or cluster.get('id') or cluster.get('cluster')
            if not cid: continue
            slug = cluster.get('slug') or slugify(cluster.get('name', cid))
            body = f"# {cluster.get('name', cid)}\n\n{cluster.get('mission','')}\n\n"
            body += "{% assign items = site.data.content.content | where: 'cluster', '" + str(cid) + "' %}\n{% for item in items %}\n### {{ item.title | default: item.user_job }}\n{{ item.learning_outcome }}\n\n{% endfor %}"
            write_page(out/'_clusters'/f'{cid}.md', {'layout':'hub','title':cluster.get('name', cid),'description':cluster.get('mission',''),'permalink':f'/{domain_id}/{slug}/','domain':domain_id,'cluster':cid}, body)
    raw_topics = topics_db.get('topics', [])
    topics = list(raw_topics.values()) if isinstance(raw_topics, dict) else raw_topics
    for topic in topics:
        tid = topic.get('topic_id')
        if not tid: continue
        slug = topic.get('slug') or slugify(topic.get('name', tid))
        body = f"# {topic.get('name', tid)}\n\n{topic.get('learning_problem','')}\n\n"
        body += "{% assign items = site.data.content.content | where: 'topic', '" + str(tid) + "' %}\n{% for item in items %}\n### {{ item.title | default: item.user_job }}\n{{ item.learning_outcome }}\n\n{% endfor %}"
        write_page(out/'_topics'/f'{tid}.md', {'layout':'hub','title':topic.get('name', tid),'description':topic.get('learning_problem',''),'permalink':f'/topics/{slug}/','topic_id':tid}, body)
    raw_paths = paths_db.get('learning_paths', [])
    paths = list(raw_paths.values()) if isinstance(raw_paths, dict) else raw_paths
    for path in paths:
        pid = path.get('path_id')
        if not pid: continue
        slug = path.get('slug') or slugify(path.get('name', pid))
        body = f"# {path.get('name', pid)}\n\n{path.get('primary_outcome','')}\n\n"
        for step in path.get('recommended_order', []):
            cid = step.get('content_id'); item = by_id.get(cid, {})
            body += f"## {step.get('step','')}. {item.get('title') or item.get('user_job') or cid}\n\n{item.get('learning_outcome','')}\n\n"
        write_page(out/'_paths'/f'{pid}.md', {'layout':'hub','title':path.get('name', pid),'description':path.get('primary_outcome',''),'permalink':f'/paths/{slug}/','path_id':pid}, body)
    manifest = {'generated_sections':len(site.get('content_sections', {})), 'generated_clusters':sum(len(d.get('clusters', {}) if isinstance(d.get('clusters', {}), dict) else d.get('clusters', [])) for d in domains), 'generated_topics':len(topics), 'generated_paths':len(paths), 'content_records':len(contents)}
    (out/'manifest.yml').write_text(yaml.safe_dump(manifest, sort_keys=False), encoding='utf-8')
    print(yaml.safe_dump(manifest, sort_keys=False))
if __name__ == '__main__': main()
