---
layout: hub
title: English levels and progression
description: Non sapere cosa significhino davvero A2, B1 e B2 o quale sia il passo
  successivo.
permalink: /topics/english-levels-and-progression/
topic_id: TOP-32
---

# English levels and progression

Non sapere cosa significhino davvero A2, B1 e B2 o quale sia il passo successivo.

{% assign items = site.data.content.content | where: 'topic', 'TOP-32' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
