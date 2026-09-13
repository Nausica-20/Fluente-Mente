---
layout: default
title: "Alternative Ways to Say… | Fluente-Mente"
description: "Alternative più naturali per evitare ripetizioni e scegliere il tono giusto."
permalink: /alternative-ways-to-say/
content_family: "alternative_ways"
---

<section class="section-start">
  <div class="container">
    <header class="section-heading">
      <p class="eyebrow">ALTERNATIVE WAYS TO SAY…</p>
      <h1>Alternative Ways to Say…</h1>
      <p>Alternative più naturali per evitare ripetizioni e scegliere il tono giusto.</p>
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
