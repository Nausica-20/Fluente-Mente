---
layout: default
title: "Travel English | Fluente-Mente"
description: "Contenuti di inglese naturale su travel: dialoghi, storie e guide pratiche."
permalink: /travel/
cluster: "travel"
---

<section class="section-start">
  <div class="container">
    <header class="section-heading">
      <p class="eyebrow">CLUSTER</p>
      <h1>Travel English</h1>
      <p>Editorial cluster for travel content.</p>
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
