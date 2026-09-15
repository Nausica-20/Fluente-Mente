---
layout: hub
title: study_system
description: Costruire un sistema di studio realistico e sostenibile.
permalink: /get_unstuck/study_system/
domain: get_unstuck
cluster: study_system
---

# study_system

Costruire un sistema di studio realistico e sostenibile.

{% assign items = site.data.content.content | where: 'cluster', 'study_system' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
