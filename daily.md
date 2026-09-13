---
layout: default
title: "365 English Entry Points | Fluente-Mente"
description: "365 contenuti di inglese naturale per italiani, organizzati per formato, topic, livello e giorno."
permalink: /daily/
---

<section class="section-start">
  <div class="container">
    <header class="section-heading">
      <p class="eyebrow">365 ENGLISH ENTRY POINTS</p>
      <h1>Your Daily English Lesson</h1>
      <p>Un contenuto al giorno, da Day 1 a Day 365, organizzato per situazione, formato e livello.</p>
    </header>

    <div class="rubrics-grid">
      {% assign daily_articles = site.articles | sort: "day" %}
      {% for article in daily_articles %}
        <article class="rubric-card">
          <div class="rubric-card-top">
            <span class="rubric-number">{{ article.day }}</span>
            <span class="rubric-label">{{ article.level }}</span>
          </div>
          <div class="rubric-card-content">
            <p class="rubric-label">{{ article.content_family }}</p>
            <h2 class="rubric-title"><a href="{{ article.url | relative_url }}">{{ article.h1 | default: article.title }}</a></h2>
            <p class="rubric-description">{{ article.learning_objective }}</p>
          </div>
          <a class="rubric-link" href="{{ article.url | relative_url }}">Leggi →</a>
        </article>
      {% endfor %}
    </div>
  </div>
</section>
