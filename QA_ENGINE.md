# Fluente-Mente QA Engine

Il QA è diviso in due livelli.

## 1. Structural QA

Automatizza:
- front matter
- sincronizzazione con content.yml
- esistenza Learning Brief
- target language
- H1 e placeholder
- SEO metadata di base
- related content
- funnel boundaries
- Pinterest metadata

```bash
python scripts/run_qa.py --root .
```

Per bloccare il processo anche sui REVIEW:

```bash
python scripts/run_qa.py --root . --fail-on-review
```

## 2. Linguistic / Editorial QA

Il prompt `prompts/QA_REVIEW_PROMPT_v1.md` guida la revisione semantica,
linguistica e didattica che non è affidabile con sole regex.

Decisioni:

PASS = pubblicabile dopo controllo finale
REVIEW = richiede correzioni
FAIL = non pubblicabile

Un articolo non passa automaticamente a `published`.
