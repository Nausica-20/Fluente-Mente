---
layout: hub
title: speaking_problems
description: Affrontare blocchi e difficoltà nello speaking.
permalink: /get_unstuck/speaking_problems/
domain: get_unstuck
cluster: speaking_problems
---

# speaking_problems

Affrontare blocchi e difficoltà nello speaking.

{% assign items = site.data.content.content | where: 'cluster', 'speaking_problems' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
