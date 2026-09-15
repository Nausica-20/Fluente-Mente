---
layout: hub
title: Restaurant communication
description: Ordinare, prenotare e chiedere informazioni in un ristorante.
permalink: /topics/restaurant-communication/
topic_id: TOP-18
---

# Restaurant communication

Ordinare, prenotare e chiedere informazioni in un ristorante.

{% assign items = site.data.content.content | where: 'topic', 'TOP-18' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
