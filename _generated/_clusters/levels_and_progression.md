---
layout: hub
title: levels_and_progression
description: Capire i livelli e orientarsi nella progressione.
permalink: /get_unstuck/levels_and_progression/
domain: get_unstuck
cluster: levels_and_progression
---

# levels_and_progression

Capire i livelli e orientarsi nella progressione.

{% assign items = site.data.content.content | where: 'cluster', 'levels_and_progression' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
