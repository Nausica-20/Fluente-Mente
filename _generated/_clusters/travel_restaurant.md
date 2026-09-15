---
layout: hub
title: travel_restaurant
description: Gestire prenotazioni, ordini e richieste al ristorante.
permalink: /english_for_real_life/travel_restaurant/
domain: english_for_real_life
cluster: travel_restaurant
---

# travel_restaurant

Gestire prenotazioni, ordini e richieste al ristorante.

{% assign items = site.data.content.content | where: 'cluster', 'travel_restaurant' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
