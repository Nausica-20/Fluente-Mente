---
layout: hub
title: learning_methods
description: Confrontare approcci e scegliere un metodo di apprendimento.
permalink: /choose_next_step/learning_methods/
domain: choose_next_step
cluster: learning_methods
---

# learning_methods

Confrontare approcci e scegliere un metodo di apprendimento.

{% assign items = site.data.content.content | where: 'cluster', 'learning_methods' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
