---
layout: hub
title: opinions_and_social
description: Esprimere opinioni e gestire accordo, disaccordo e conversazioni sociali.
permalink: /use_english/opinions_and_social/
domain: use_english
cluster: opinions_and_social
---

# opinions_and_social

Esprimere opinioni e gestire accordo, disaccordo e conversazioni sociali.

{% assign items = site.data.content.content | where: 'cluster', 'opinions_and_social' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
