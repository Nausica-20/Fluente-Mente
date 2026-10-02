#!/usr/bin/env python3
from pathlib import Path
import argparse, yaml

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); args=ap.parse_args(); root=Path(args.root)
    reg=yaml.safe_load((root/'_data/content_registry.yml').read_text(encoding='utf-8'))
    entries=reg.get('entries',[])
    manifest={
      'schema':'fluente-mente-physical-site-manifest-v1',
      'registry_records':len(entries),
      'physical_record_routes':sum((root/e['url'].strip('/')/'index.md').exists() for e in entries),
      'generated_at_rule':'runtime-generated during CI',
      'status':'ready_for_jekyll_build'
    }
    (root/'BUILD_MANIFEST.yml').write_text(yaml.safe_dump(manifest,sort_keys=False),encoding='utf-8')
    print(yaml.safe_dump(manifest,sort_keys=False))
if __name__=='__main__': main()
