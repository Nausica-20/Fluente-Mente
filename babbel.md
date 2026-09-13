---
layout: default
title: "Babbel | Fluente-Mente"
description: "Il passo successivo verso uno studio più strutturato dell'inglese."
permalink: /babbel/
commercial: true
---

<section class="home-babbel">
  <div class="container">
    <div class="babbel-home-card">
      <div class="babbel-home-copy">
        <p class="eyebrow">UN PASSO IN PIÙ</p>
        <h1 class="babbel-home-title">Vuoi una pratica più strutturata?</h1>
        <p>
          Fluente-Mente è pensato per aiutarti a usare l'inglese in contesto.
          Babbel può affiancare questo percorso con una pratica più strutturata.
        </p>
        <div class="home-cta-row">
          {% if site.babbel.default_destination %}
            <a class="button button-primary" href="{{ site.babbel.default_destination }}" rel="sponsored nofollow" target="_blank">Scopri Babbel</a>
          {% endif %}
        </div>
      </div>
      <div class="babbel-home-note">
        <strong>Trasparenza</strong>
        <p>{{ site.babbel.disclosure.text }}</p>
      </div>
    </div>
  </div>
</section>
