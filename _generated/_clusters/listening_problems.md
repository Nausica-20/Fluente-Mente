---
layout: hub
title: listening_problems
description: Capire meglio l'inglese parlato reale.
permalink: /get_unstuck/listening_problems/
domain: get_unstuck
cluster: listening_problems
---

# listening_problems

Capire meglio l'inglese parlato reale.

{% assign items = site.data.content.content | where: 'cluster', 'listening_problems' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
