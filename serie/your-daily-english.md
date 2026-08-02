---
layout: default
title: "Your Daily English — 365 giorni di inglese"
description: "Un piccolo appuntamento quotidiano per imparare parole, frasi ed espressioni inglesi utili e trasformare l'inglese in una pratica quotidiana."
permalink: /serie/your-daily-english/
series_id: "your-daily-english"
---

{% assign current_series = site.data.site.series | where: "id", page.series_id | first %}

{% if current_series %}

<!-- ==================================================
     BREADCRUMB
     ================================================== --><nav class="breadcrumbs" aria-label="Breadcrumb">  <a href="{{ site.data.site.urls.home | relative_url }}">
    Home
  </a><span aria-hidden="true">→</span>

  <a href="{{ site.data.site.urls.series | relative_url }}">
    Serie
  </a><span aria-hidden="true">→</span>

  <span>
    {{ current_series.title }}
  </span></nav><!-- ==================================================
     HERO SERIE
     ================================================== --><section class="hero">  <div class="container hero-inner"><span class="hero-label">
  Serie {{ current_series.number | prepend: "0" | slice: -2, 2 }}
</span>

<h1>
  {{ current_series.title }}
</h1>

{% if current_series.tagline %}

<p class="hero-description">
  {{ current_series.tagline }}
</p>

{% endif %}

{% if current_series.description %}

<p class="hero-description">
  {{ current_series.description }}
</p>

{% endif %}

  </div></section><!-- ==================================================
     INTRO / OBIETTIVO
     ================================================== --><section class="series-info">  <div class="container"><header class="section-heading">

  <span class="section-label">
    IL PERCORSO
  </span>

  <h2>
    Inglese ogni giorno, un passo alla volta
  </h2>

  <p>
    Your Daily English nasce per trasformare
    l'inglese da qualcosa che studi ogni tanto
    in una piccola abitudine quotidiana.
  </p>

  <p>
    Ogni contenuto ti permette di imparare,
    ripassare o usare qualcosa di concreto
    senza dover dedicare ore allo studio.
  </p>

</header>

  </div></section><!-- ==================================================
     INFO SERIE
     ================================================== --><section class="series-info">  <div class="container"><div class="series-info-grid">

  {% if current_series.audience %}

  <article class="series-info-item">

    <span class="section-label">
      PER CHI
    </span>

    <h2>
      A chi è dedicata
    </h2>

    <p>
      {{ current_series.audience }}
    </p>

  </article>

  {% endif %}


  {% if current_series.goal %}

  <article class="series-info-item">

    <span class="section-label">
      OBIETTIVO
    </span>

    <h2>
      Cosa puoi ottenere
    </h2>

    <p>
      {{ current_series.goal }}
    </p>

  </article>

  {% endif %}


  {% if current_series.format %}

  <article class="series-info-item">

    <span class="section-label">
      FORMATO
    </span>

    <h2>
      Come funziona
    </h2>

    <p>
      {{ current_series.format }}
    </p>

  </article>

  {% endif %}

</div>

  </div></section><!-- ==================================================
     ARTICOLI
     ================================================== --><section class="series-articles">  <div class="container"><header class="section-heading">

  <span class="section-label">
    YOUR DAILY ENGLISH
  </span>

  <h2>
    Gli articoli della serie
  </h2>

  <p>
    Segui gli appuntamenti uno alla volta
    e costruisci la tua pratica quotidiana
    di inglese.
  </p>

</header>


{% assign series_posts = site.posts | where: "series", current_series.id %}


{% if series_posts.size > 0 %}

<div class="series-grid">

  {% for post in series_posts %}

  <article class="series-card">

    {% if post.category %}

    <span class="series-number">
      {{ post.category }}
    </span>

    {% endif %}

    <h3>

      <a href="{{ post.url | relative_url }}">
        {{ post.title }}
      </a>

    </h3>

    {% if post.description %}

    <p>
      {{ post.description }}
    </p>

    {% elsif post.excerpt %}

    <p>
      {{ post.excerpt | strip_html | truncate: 160 }}
    </p>

    {% endif %}

    <a
      href="{{ post.url | relative_url }}"
      class="card-link"
    >
      Leggi l'articolo →
    </a>

  </article>

  {% endfor %}

</div>


{% else %}

<div class="empty-state">

  <h3>
    Gli articoli stanno arrivando
  </h3>

  <p>
    La serie sarà costruita progressivamente
    con nuovi appuntamenti quotidiani.
  </p>

</div>

{% endif %}

  </div></section><!-- ==================================================
     NAVIGAZIONE TRA LE SERIE
     ================================================== --><section class="series-navigation">  <div class="container">{% assign previous_number = current_series.number | minus: 1 %}
{% assign next_number = current_series.number | plus: 1 %}

{% assign previous_series = site.data.site.series
  | where: "number", previous_number
  | first %}

{% assign next_series = site.data.site.series
  | where: "number", next_number
  | first %}


{% if previous_series %}

<a
  href="{{ previous_series.permalink | relative_url }}"
  class="series-nav previous"
>
  ← {{ previous_series.title }}
</a>

{% endif %}


<a
  href="{{ site.data.site.urls.series | relative_url }}"
  class="series-nav all-series"
>
  Tutte le serie
</a>


{% if next_series %}

<a
  href="{{ next_series.permalink | relative_url }}"
  class="series-nav next"
>
  {{ next_series.title }} →
</a>

{% endif %}

  </div></section><!-- ==================================================
     METODO
     ================================================== --><section class="method-preview">  <div class="container"><header class="section-heading">

  <span class="section-label">
    METODO FLUENTE-MENTE
  </span>

  <h2>
    Vuoi trasformare l'inglese in una routine?
  </h2>

  <p>
    Scopri il metodo Fluente-Mente per imparare,
    praticare e usare l'inglese in modo semplice
    e sostenibile.
  </p>

</header>

<a
  href="{{ site.data.site.urls.method | relative_url }}"
  class="button button-primary"
>
  Scopri il metodo
</a>

  </div></section>{% endif %}
