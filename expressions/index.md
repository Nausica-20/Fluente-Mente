---
layout: hub
title: Expressions
description: Le 365 espressioni del corpus Fluente-Mente, organizzate e ricercabili
  senza creare pagine duplicate.
permalink: /expressions/
index: true
follow: true
sitemap: true
content_id: IDX-EXPRESSIONS
content_type: expressions_index
canonical: /expressions/
status: published
---

## Il database delle espressioni

Le espressioni sono **entità dati**: la loro pagina didattica canonica è la relativa Pillola del Giorno.

<div class="content-directory" data-filter-list>
{% for e in site.data.expressions.expressions %}<article class="content-card" data-filter-item data-search="{{ e.expression | downcase }} {{ e.meaning_it | default: '' | downcase }} {{ e.topic | default: '' | downcase }}"><p class="eyebrow">{{ e.level }}</p><h3>{{ e.expression }}</h3><p>{{ e.meaning_it }}</p>{% if e.article_url %}<a href="{{ e.article_url | relative_url }}">Vai alla Pillola →</a>{% endif %}</article>{% endfor %}
</div>
