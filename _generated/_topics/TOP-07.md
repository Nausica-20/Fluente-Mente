---
layout: hub
title: Talking about plans and weekends
description: Parlare di programmi futuri nelle conversazioni informali.
permalink: /topics/talking-about-plans-and-weekends/
topic_id: TOP-07
---

# Talking about plans and weekends

Parlare di programmi futuri nelle conversazioni informali.

{% assign items = site.data.content.content | where: 'topic', 'TOP-07' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
