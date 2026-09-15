---
layout: hub
title: Everyday expressions and reactions
description: Non riconoscere espressioni brevi che i madrelingua usano continuamente.
permalink: /topics/everyday-expressions-and-reactions/
topic_id: TOP-08
---

# Everyday expressions and reactions

Non riconoscere espressioni brevi che i madrelingua usano continuamente.

{% assign items = site.data.content.content | where: 'topic', 'TOP-08' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
