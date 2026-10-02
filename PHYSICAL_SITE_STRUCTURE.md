# Fluente-Mente — Physical Site Structure

## Base tecnica

La struttura tecnica deriva dal repository ZIP `Fluente-Mente-main.zip`: Jekyll, GitHub Pages, workflow GitHub Actions, layout, include, Sass, asset e sistema visuale vengono mantenuti come base.

## Materializzazione del registry

Il registry operativo corrente contiene 841 record. Ogni record è materializzato nella propria route:

```text
<route-canonica>/index.md
```

Validazione corrente: **841 record / 841 file fisici**, con ID, slug e URL unici.

## Contenuti

```text
pills/                         365 pagine + indice
situations/                     52 pagine + indice
grammar/                        52 pagine + indice
non-sono-la-stessa-cosa/       259 pagine + indice
travel-english/                 26 pagine
business-english/               26 pagine
english-culture/                24 pagine
inglese-da-adulti/              24 pagine
babbel/                          7 pagine
expressions/                     1 indice
words/                           1 indice
```

Totale: **835 contenuti + 6 indici = 841 record registrati**.

## Strato di supporto

Restano le pagine non editoriali del progetto originale, riorganizzate come servizi del sito:

```text
about/
contact/
privacy/
cookie/
affiliate-disclosure/
editorial-policy/
choose/
paths/
levels/
search/
```

Queste pagine non fanno parte dei 841 record del registry.

## Dati

```text
_data/content_registry.yml
_data/master_content_architecture.yml
_data/content_mapping.yml
_data/daily_pills.yml
_data/situational.yml
_data/situational_grammar.yml
_data/confusione_front_matters.yml
_data/expressions.yml
_data/architectures/*.yml
```

Le espressioni sono entità dati: la loro destinazione didattica canonica è la relativa Pillola.

La fonte autorevole delle parole non è ancora definita; `/words/` resta quindi un indice strutturale senza database inventato.

## Rimossi nel rebuild

Le vecchie sezioni editoriali del repository originale non sono state mantenute perché non appartengono all'architettura canonica corrente:

```text
english/
real-english/
english-for-real-life/
english-learning/
learn-english/
_generated/
```

## Produzione

`_articles/` resta solo come workspace per bozze. Le pagine pubblicabili vivono nelle route canoniche fisiche del repository.
