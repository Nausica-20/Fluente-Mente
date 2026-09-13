---
layout: default
title: "Study English | Fluente-Mente"
description: "Contenuti di inglese naturale su study: dialoghi, storie e guide pratiche."
permalink: /study/
cluster: "study"
---

<section class="section-start">
  <div class="container">
    <header class="section-heading">
      <p class="eyebrow">CLUSTER</p>
      <h1>Study English</h1>
      <p>Editorial cluster for study content.</p>
    </header>

    <div class="rubrics-grid">
      {% assign cluster_articles = site.articles | where: "cluster", page.cluster | sort: "day" %}
      {% for article in cluster_articles %}
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
