---
layout: hub
title: Social English
description: Difficoltà a creare e gestire interazioni sociali in inglese.
permalink: /topics/social-english/
topic_id: TOP-22
---

# Social English

Difficoltà a creare e gestire interazioni sociali in inglese.

{% assign items = site.data.content.content | where: 'topic', 'TOP-22' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
