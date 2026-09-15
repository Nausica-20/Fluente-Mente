---
layout: hub
title: Vocabulary retention
description: Imparare parole nuove e dimenticarle rapidamente.
permalink: /topics/vocabulary-retention/
topic_id: TOP-28
---

# Vocabulary retention

Imparare parole nuove e dimenticarle rapidamente.

{% assign items = site.data.content.content | where: 'topic', 'TOP-28' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
