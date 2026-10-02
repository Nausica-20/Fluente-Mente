# Fluente-Mente — Content Writer Engine

Il repository distingue tra **struttura fisica del sito**, **registry operativo** e **testo degli articoli**.

## Sorgenti

- `_data/master_content_architecture.yml` — gerarchia, ownership, route e regole globali.
- `_data/content_registry.yml` — 841 record pubblicabili e stato operativo.
- `_data/architectures/` — contratti editoriali per le singole aree.
- `_data/expressions.yml` — entità linguistiche; non crea pagine individuali.

## Route canoniche

Ogni record del registry è materializzato fisicamente come:

`/<route-canonica>/index.md`

Il testo definitivo viene scritto nella stessa `index.md`; non viene creata una seconda pagina sotto `_articles`.

## `_articles/`

`_articles/` è una workspace opzionale per bozze e pacchetti di produzione. Non è una collection Jekyll pubblicata.
