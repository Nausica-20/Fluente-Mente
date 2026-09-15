---
layout: hub
title: English prepositions
description: Scegliere la preposizione corretta per influenza dell'italiano o per
  apprendimento frammentario.
permalink: /topics/english-prepositions/
topic_id: TOP-13
---

# English prepositions

Scegliere la preposizione corretta per influenza dell'italiano o per apprendimento frammentario.

{% assign items = site.data.content.content | where: 'topic', 'TOP-13' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
