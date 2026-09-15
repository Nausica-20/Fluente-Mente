# Fluente-Mente — Article Schema v2.0

## Files
- `_data/content.yml`: source of truth dei contenuti con contratto definitivo.
- `schemas/article.schema.yml`: schema YAML canonico.
- `scripts/validate_yml.py`: validator per registry e front matter Jekyll.
- `.github/workflows/validate-content.yml`: controllo automatico GitHub Actions.

## Uso locale
```bash
python scripts/validate_yml.py --root .
```

Modalità rigorosa per trasformare i warning cross-file in errori:
```bash
python scripts/validate_yml.py --root . --strict
```

## GitHub Actions
Il workflow `Validate content schema` viene eseguito automaticamente su:
- push verso `main` o `master`;
- pull request verso `main` o `master`;
- avvio manuale dal tab Actions.

Il controllo standard blocca il job quando il validator trova errori. I warning cross-file restano visibili ma non bloccano il workflow finché non vengono risolti.

Il controllo `--strict` viene eseguito come step informativo e non blocca il workflow: serve a mostrare in anticipo quali warning diventerebbero errori nella fase di hardening della tassonomia.

## Regola di integrazione
Il workflow deve essere eseguito prima del deploy del sito. Quando verrà aggiunto il workflow Jekyll di produzione, il job di build/deploy dovrà dipendere da questo controllo (`needs: validate`).

I campi didattici possono rimanere vuoti in `content.yml` durante la fase di planning; diventano obbligatori negli articoli Jekyll per i content type didattici.
