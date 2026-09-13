---
layout: default
title: "Dialogues | Fluente-Mente"
description: "Conversazioni realistiche per affrontare situazioni concrete in inglese."
permalink: /dialogues/
content_family: "dialogue"
---

<section class="section-start">
  <div class="container">
    <header class="section-heading">
      <p class="eyebrow">DIALOGUES</p>
      <h1>Dialogues</h1>
      <p>Conversazioni realistiche per affrontare situazioni concrete in inglese.</p>
    </header>

    <div class="rubrics-grid">
      {% assign family_articles = site.articles | where: "content_family", page.content_family | sort: "day" %}
      {% for article in family_articles %}
        <article class="rubric-card">
          <div class="rubric-card-top">
            <span class="rubric-number">{{ article.day }}</span>
            <span class="rubric-label">{{ article.level }}</span>
          </div>
          <div class="rubric-card-content">
            <h2 class="rubric-title">
              <a href="{{ article.url | relative_url }}">{{ article.h1 | default: article.title }}</a>
            </h2>
            <p class="rubric-description">{{ article.learning_objective }}</p>
          </div>
          <a class="rubric-link" href="{{ article.url | relative_url }}">Leggi →</a>
        </article>
      {% endfor %}
    </div>
  </div>
</section>
