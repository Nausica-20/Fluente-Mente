---
layout: default
title: "Fluente-Mente | Impara. Pratica. Comunica."
description: "Guide pratiche e strategie semplici per imparare l'inglese e le lingue, anche con poco tempo."
---

<section class="hero">

  <div class="hero__content">

    <p class="hero__eyebrow">FLUENTE-MENTE</p>

    <h1>Impara una lingua.<br>Un passo alla volta.</h1>

    <p class="hero__text">
      Guide pratiche, metodi semplici e risorse utili
      per migliorare una lingua anche quando hai poco tempo.
    </p>

    <div class="hero__buttons">

      <a href="{{ '/inglese/' | relative_url }}" class="button">
        Inizia dall'inglese
      </a>

      <a href="{{ '/metodo/' | relative_url }}" class="button button--secondary">
        Scopri il metodo
      </a>

    </div>

  </div>

</section>


<section class="intro">

  <div class="container">

    <h2>Imparare una lingua può essere più semplice</h2>

    <p>
      Non servono ore di studio ogni giorno.
      Serve un metodo che riesci a mantenere.
    </p>

    <p>
      Su Fluente-Mente trovi spiegazioni chiare, esempi pratici
      e strategie pensate per chi vuole imparare una lingua
      nella vita reale.
    </p>

  </div>

</section>


<section class="categories">

  <div class="container">

    <h2>Da dove vuoi iniziare?</h2>

    <div class="category-grid">

      <a href="{{ '/inglese/' | relative_url }}" class="category-card">

        <span class="category-card__icon">🇬🇧</span>

        <h3>Inglese</h3>

        <p>
          Grammatica, vocabolario, speaking,
          pronuncia e inglese per viaggiare.
        </p>

        <span class="category-card__link">
          Scopri l'inglese →
        </span>

      </a>


      <a href="{{ '/metodo/' | relative_url }}" class="category-card">

        <span class="category-card__icon">🧠</span>

        <h3>Metodo</h3>

        <p>
          Strategie per studiare meglio,
          creare una routine e mantenere la motivazione.
        </p>

        <span class="category-card__link">
          Scopri il metodo →
        </span>

      </a>


      <a href="{{ '/viaggio/' | relative_url }}" class="category-card">

        <span class="category-card__icon">✈️</span>

        <h3>Viaggio</h3>

        <p>
          Frasi, vocaboli e situazioni utili
          per comunicare durante i tuoi viaggi.
        </p>

        <span class="category-card__link">
          Inglese per viaggiare →
        </span>

      </a>


      <a href="{{ '/lingue/' | relative_url }}" class="category-card">

        <span class="category-card__icon">🌍</span>

        <h3>Lingue</h3>

        <p>
          Scopri metodi e risorse per imparare
          nuove lingue e ampliare i tuoi orizzonti.
        </p>

        <span class="category-card__link">
          Scopri le lingue →
        </span>

      </a>

    </div>

  </div>

</section>


<section class="method">

  <div class="container">

    <p class="section-label">IL METODO FLUENTE-MENTE</p>

    <h2>Piccoli passi. Ogni giorno.</h2>

    <p>
      Imparare una lingua non significa studiare tutto
      contemporaneamente.
    </p>

    <div class="steps">

      <div class="step">

        <span class="step__number">01</span>

        <h3>Impara</h3>

        <p>
          Scopri nuove parole, frasi e strutture.
        </p>

      </div>


      <div class="step">

        <span class="step__number">02</span>

        <h3>Pratica</h3>

        <p>
          Utilizza ciò che hai imparato attraverso
          ascolto, lettura e conversazione.
        </p>

      </div>


      <div class="step">

        <span class="step__number">03</span>

        <h3>Comunica</h3>

        <p>
          Porta la lingua nella vita reale.
        </p>

      </div>

    </div>

  </div>

</section>


<section class="latest">

  <div class="container">

    <h2>Dal blog</h2>

    <p>
      Guide e articoli per aiutarti a migliorare
      la tua lingua passo dopo passo.
    </p>

    <div class="post-list">

      {% for post in site.posts limit:6 %}

        <article class="post-card">

          <p class="post-card__category">
            {{ post.category }}
          </p>

          <h3>
            <a href="{{ post.url | relative_url }}">
              {{ post.title }}
            </a>
          </h3>

          {% if post.description %}
            <p>{{ post.description }}</p>
          {% else %}
            <p>{{ post.excerpt | strip_html | truncate: 140 }}</p>
          {% endif %}

          <a href="{{ post.url | relative_url }}">
            Leggi l'articolo →
          </a>

        </article>

      {% endfor %}

    </div>

  </div>

</section>


<section class="cta">

  <div class="container">

    <h2>Vuoi creare una routine di studio?</h2>

    <p>
      Una pratica breve e regolare può aiutarti
      a trasformare lo studio della lingua in un'abitudine.
    </p>

    <a href="#" class="button">
      Scopri Babbel
    </a>

    <p class="cta__note">
      Link affiliato. Se acquisti attraverso il link,
      Fluente-Mente potrebbe ricevere una commissione
      senza costi aggiuntivi per te.
    </p>

  </div>

</section>
