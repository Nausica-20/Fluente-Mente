# Fluente-Mente — Article Production Engine v1

Pipeline: `content.yml` + `_data/learning_briefs.yml` + `_data/learning_briefs/*.yml` → production packets → QA gate.

The engine does **not** invent pedagogical targets and does **not** publish automatically.

## Commands

```bash
pip install pyyaml
python scripts/build_production_packets.py --root .
python scripts/validate_production_packets.py --root .
```

Expected: 119 production packets and 0 QA errors with the current normalized dataset.

Generated packets are under `_articles/generated/`; the final editorial step produces Markdown articles from the packets and sends them through the QA gate before publication.
