# Fluente-Mente — Physical Site Rebuild

Questa repository è stata riscritta da zero partendo dalla base Jekyll/visual del file ZIP fornito e materializzando le route del registry corrente

## Principi

- Jekyll + GitHub Pages
- contenuti canonici come directory `/<sezione>/<slug>/index.md`
- 841 record fisici corrispondenti a 841 record del registry
- 6 indici dedicati
- database delle espressioni senza pagine duplicate
- fonte delle parole non inventata finché non viene definita nel Master Content Architecture
- Babbel separato dal motore editoriale
- draft e produzione separati dalle pagine canoniche

## Comandi CI locali

```bash
python scripts/validate_yml.py --root .
python scripts/generate_site.py --root .
```

La build Jekyll finale viene eseguita da GitHub Actions con Ruby/Bundler.
