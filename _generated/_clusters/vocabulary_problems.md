---
layout: hub
title: vocabulary_problems
description: Migliorare memorizzazione e recupero del vocabolario.
permalink: /get_unstuck/vocabulary_problems/
domain: get_unstuck
cluster: vocabulary_problems
---

# vocabulary_problems

Migliorare memorizzazione e recupero del vocabolario.

{% assign items = site.data.content.content | where: 'cluster', 'vocabulary_problems' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
