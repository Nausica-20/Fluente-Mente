---
layout: default
title: "Blog"
description: "Articoli pratici per imparare e usare l'inglese nella vita reale."
permalink: /blog/
---

<section class="page-header">

  <div class="container">

    <span class="section-label">
      FLUENTE-MENTE
    </span>

    <h1>
      Blog
    </h1>

    <p class="page-description">
      Guide, spiegazioni, consigli e strategie
      per migliorare il tuo inglese in modo pratico.
    </p>

  </div>

</section>


<section class="blog-list">

  <div class="container">

    {% if site.posts.size > 0 %}

      <div class="post-list">

        {% for post in site.posts %}

          <article class="post-card">

            <div class="post-card-content">

              {% if post.series %}

                {% assign current_series = site.data.site.series
                  | where: "id", post.series
                  | first
                %}

                {% if current_series %}

                  <span class="post-series">
                    {{ current_series.title }}
                  </span>

                {% endif %}

              {% endif %}


              <h2>

                <a href="{{ post.url | relative_url }}">
                  {{ post.title }}
                </a>

              </h2>


              {% if post.description %}

                <p>
                  {{ post.description }}
                </p>

              {% endif %}


              <div class="post-meta">

                <time datetime="{{ post.date | date_to_xmlschema }}">
                  {{ post.date | date: "%d/%m/%Y" }}
                </time>

              </div>


              <a
                href="{{ post.url | relative_url }}"
                class="card-link"
              >
                Leggi l'articolo
              </a>

            </div>

          </article>

        {% endfor %}

      </div>

    {% else %}

      <p class="empty-state">
        I primi articoli di Fluente-Mente arriveranno presto.
      </p>

    {% endif %}

  </div>

</section>
