---
layout: hub
title: babbel_core
description: Spiegare come funziona Babbel e per quali profili può essere utile.
permalink: /choose_next_step/babbel_core/
domain: choose_next_step
cluster: babbel_core
---

# babbel_core

Spiegare come funziona Babbel e per quali profili può essere utile.

{% assign items = site.data.content.content | where: 'cluster', 'babbel_core' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
