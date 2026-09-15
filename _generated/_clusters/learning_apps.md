---
layout: hub
title: learning_apps
description: Valutare le app per l'apprendimento delle lingue in base a bisogni concreti.
permalink: /choose_next_step/learning_apps/
domain: choose_next_step
cluster: learning_apps
---

# learning_apps

Valutare le app per l'apprendimento delle lingue in base a bisogni concreti.

{% assign items = site.data.content.content | where: 'cluster', 'learning_apps' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
