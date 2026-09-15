---
layout: hub
title: Opinions and polite disagreement
description: Esprimere opinioni e dissentire senza sembrare troppo diretti.
permalink: /topics/opinions-and-polite-disagreement/
topic_id: TOP-06
---

# Opinions and polite disagreement

Esprimere opinioni e dissentire senza sembrare troppo diretti.

{% assign items = site.data.content.content | where: 'topic', 'TOP-06' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
