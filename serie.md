---
layout: default
title: "Serie di inglese"
description: "Percorsi pratici per imparare, ripassare e usare l'inglese nella vita reale."
permalink: /serie/
---

<section class="page-header">  <div class="container"><span class="section-label">
  FLUENTE-MENTE
</span>

<h1>
  Serie di inglese
</h1>

<p class="page-description">
  Scegli un percorso e inizia da ciò che ti serve
  davvero: inglese quotidiano, conversazione,
  viaggio, grammatica, vocaboli e metodo.
</p>

  </div></section><!-- ==================================================
     INTRO
     ================================================== --><section class="intro">  <div class="container"><div class="section-heading">

  <span class="section-label">
    SCEGLI IL TUO PERCORSO
  </span>

  <h2>
    Impara l'inglese un passo alla volta
  </h2>

  <p>
    Le Serie di Fluente-Mente raccolgono articoli
    collegati tra loro e organizzati intorno a un
    obiettivo concreto.
  </p>

  <p>
    Non devi seguire tutto.
    Scegli la serie più vicina alle tue esigenze
    e costruisci il tuo percorso.
  </p>

</div>

  </div></section><!-- ==================================================
     TUTTE LE SERIE
     ================================================== --><section class="series-list">  <div class="container"><header class="section-heading">

  <span class="section-label">
    11 PERCORSI
  </span>

  <h2>
    Tutte le Serie
  </h2>

  <p>
    Ogni serie affronta un aspetto diverso
    dell'apprendimento e dell'uso dell'inglese.
  </p>

</header>


{% assign series_list = site.data.site.series | sort: "number" %}

<div class="series-grid">

  {% for series in series_list %}

    <article class="series-card">

      <span class="series-number">
        {{ series.number | prepend: "0" | slice: -2, 2 }}
      </span>

      <h2>
        {{ series.title }}
      </h2>

      {% if series.tagline %}

        <p class="series-tagline">
          {{ series.tagline }}
        </p>

      {% endif %}

      {% if series.short_description %}

        <p>
          {{ series.short_description }}
        </p>

      {% elsif series.description %}

        <p>
          {{ series.description }}
        </p>

      {% endif %}

      <a
        href="{{ series.permalink | relative_url }}"
        class="card-link"
        aria-label="Scopri la serie {{ series.title }}"
      >
        Scopri la serie →
      </a>

    </article>

  {% endfor %}

</div>

  </div></section><!-- ==================================================
     METODO
     ================================================== --><section class="method-preview">  <div class="container"><header class="section-heading">

  <span class="section-label">
    IL METODO FLUENTE-MENTE
  </span>

  <h2>
    Non sai da dove iniziare?
  </h2>

  <p>
    Parti dal metodo Fluente-Mente e scopri come
    combinare comprensione, apprendimento,
    pratica e continuità.
  </p>

</header>

<a
  href="{{ site.data.site.urls.method | relative_url }}"
  class="button button-primary"
>
  Scopri il metodo
</a>

  </div></section>
