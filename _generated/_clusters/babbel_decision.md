---
layout: hub
title: babbel_decision
description: Aiutare l’utente a capire quando Babbel è o non è una scelta adatta.
permalink: /choose_next_step/babbel_decision/
domain: choose_next_step
cluster: babbel_decision
---

# babbel_decision

Aiutare l’utente a capire quando Babbel è o non è una scelta adatta.

{% assign items = site.data.content.content | where: 'cluster', 'babbel_decision' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
