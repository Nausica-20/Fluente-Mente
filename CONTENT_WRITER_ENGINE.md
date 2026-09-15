# Fluente-Mente Content Writer Engine

Pipeline:

content.yml
→ learning_briefs.yml
→ production packets
→ Content Writer Engine
→ _articles/drafts/
→ Writer QA
→ editorial review
→ publish

Il motore non pubblica automaticamente.

## Generazione

```bash
python scripts/build_articles.py --root .
```

Per un solo contenuto:

```bash
python scripts/build_articles.py --root . --content-id UE-001
```

## QA

```bash
python scripts/validate_articles.py --root . --fail-on-placeholder
```

## Regola editoriale

Il writer engine prepara il testo. Il passaggio QA linguistico/editoriale resta
obbligatorio prima di cambiare `status` da `drafting` a `qa` e successivamente `published`.
