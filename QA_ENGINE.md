# Fluente-Mente — QA Engine

La QA strutturale verifica:

1. 841 record nel registry.
2. ID, slug e URL unici.
3. Una `index.md` fisica per ogni URL canonico.
4. Presenza dei sei indici dedicati.
5. Coerenza delle principali sorgenti YAML.
6. Assenza delle vecchie route editoriali rimosse dal rebuild.

Comando:

```bash
python scripts/validate_yml.py --root .
```
