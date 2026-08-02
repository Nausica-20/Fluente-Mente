---
layout: default
title: "Serie di inglese"
description: "Percorsi e serie pratiche per imparare, ripassare e usare l'inglese nella vita reale."
permalink: /serie/
---

<section class="page-header">

  <div class="container">

    <span class="section-label">
      FLUENTE-MENTE
    </span>

    <h1>
      Serie
    </h1>

    <p class="page-description">
      Percorsi tematici per imparare l'inglese
      attraverso lezioni pratiche, situazioni reali
      e piccoli passi sostenibili.
    </p>

  </div>

</section>


<section class="series-list">

  <div class="container">

    <div class="series-grid">

      {% for series in site.data.site.series %}

        <article class="series-card">

          <span class="series-number">
            {{ series.number | prepend: '0' | slice: -2, 2 }}
          </span>

          <h2>
            {{ series.title }}
          </h2>

          {% if series.tagline %}

            <p class="series-tagline">
              {{ series.tagline }}
            </p>

          {% endif %}

          <p>
            {{ series.description }}
          </p>

          <a
            href="{{ series.permalink | relative_url }}"
            class="card-link"
          >
            Scopri la serie
          </a>

        </article>

      {% endfor %}

    </div>

  </div>

</section>
