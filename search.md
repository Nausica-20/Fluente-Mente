---
layout: default
title: "Cerca"
description: "Cerca lezioni, espressioni e situazioni di inglese naturale su Fluente-Mente."
permalink: /search/
---

<section class="section search-page">
  <div class="container reading-container">

    <header class="section-heading">
      <p class="eyebrow">Fluente-Mente</p>
      <h1>Cerca una lezione</h1>
      <p>
        Cerca una parola, un'espressione, una situazione o un argomento
        per trovare l'inglese che vuoi usare davvero.
      </p>
    </header>

    <div class="search-box">
      <label for="search-input">Cosa vuoi cercare?</label>

      <input
        id="search-input"
        type="search"
        name="q"
        placeholder="Es. weekend, friends, restaurant..."
        autocomplete="off"
        spellcheck="false"
        aria-describedby="search-status"
      />
    </div>

    <div
      id="search-status"
      class="search-status"
      aria-live="polite"
    ></div>

    <div id="search-results" class="search-results"></div>

  </div>
</section>

<script id="search-index" type="application/json">
[
  {% for article in site.articles %}
  {
    "title": {{ article.title | jsonify }},
    "description": {{ article.description | default: "" | jsonify }},
    "url": {{ article.url | relative_url | jsonify }},
    "rubric": {{ article.rubric | default: "" | jsonify }},
    "macro_theme": {{ article.macro_theme | default: "" | jsonify }},
    "level": {{ article.level | default: "" | jsonify }},
    "keywords": {{ article.keywords | default: empty | jsonify }}
  }{% unless forloop.last %},{% endunless %}
  {% endfor %}
]
</script>

<script src="{{ '/assets/js/search.js' | relative_url }}" defer></script>
