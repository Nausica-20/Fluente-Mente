---
layout: hub
title: Thinking in English
description: Tradurre mentalmente ogni frase prima di parlare.
permalink: /topics/thinking-in-english/
topic_id: TOP-30
---

# Thinking in English

Tradurre mentalmente ogni frase prima di parlare.

{% assign items = site.data.content.content | where: 'topic', 'TOP-30' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
