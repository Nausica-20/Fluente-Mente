---
layout: hub
title: Inglese naturale
description: Capire e usare l'inglese naturale.
permalink: /real-english/
domain: understand_real_english
---

# Inglese naturale

Capire e usare l'inglese naturale.

{% assign items = site.data.content.content | where: 'domain', 'understand_real_english' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
