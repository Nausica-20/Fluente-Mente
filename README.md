# Fluente-Mente — Main Site Updated

Questa versione mantiene la base visuale di `Fluente-Mente-main` — includes, layouts, Sass, JavaScript e logo — e la collega al nuovo Content Plan + Data Architecture.

## Nuova architettura

`Pinterest → Article → Related content → Babbel`

Le quattro content family sono:
- Dialogues: 100
- Stories in English: 85
- Talking About [X]: 95
- Alternative Ways to Say…: 85

## Data layer

Il database principale è `_data/content.yml`.
Le tassonomie e le relazioni sono in `_data/`.
Il registry centrale è `_data/content_registry.yml`.
Il linking editoriale è in `_data/internal_links.yml`.
Pinterest e funnel Babbel sono centralizzati nei rispettivi file.

## Presentation layer

Sono stati preservati i componenti esistenti in `_includes/` e `_layouts/`.
Gli include sono stati adattati al nuovo modello:
`article_id → family → cluster → topic → related content → Pinterest → Babbel`.

## Articles

`_articles/` contiene 365 shell Markdown con front matter completo.
I body degli articoli sono lasciati volutamente come placeholder.

## Hubs

Family hubs:
- `/dialogues/`
- `/stories/`
- `/talking-about/`
- `/alternative-ways-to-say/`

Sono presenti inoltre i 16 cluster hub derivati da `_data/clusters.yml`.

## Validation

PASS:
- 365 record
- 365 article shells
- 365 giorni
- 365 ID
- 365 slug
- include/layout principali presenti
- data layer presente
- family hub presenti
- cluster hub presenti

Nota: un build Jekyll locale non è stato eseguito perché Bundler/Jekyll non è installato nell'ambiente corrente.
