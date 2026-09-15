---
layout: hub
title: Scegli il tuo prossimo passo
description: Scegliere metodo, strumento o percorso.
permalink: /choose/
domain: choose_next_step
---

# Scegli il tuo prossimo passo

Scegliere metodo, strumento o percorso.

{% assign items = site.data.content.content | where: 'domain', 'choose_next_step' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
