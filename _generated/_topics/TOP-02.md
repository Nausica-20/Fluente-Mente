---
layout: hub
title: Introducing yourself
description: Presentarsi in inglese con informazioni semplici ma naturali.
permalink: /topics/introducing-yourself/
topic_id: TOP-02
---

# Introducing yourself

Presentarsi in inglese con informazioni semplici ma naturali.

{% assign items = site.data.content.content | where: 'topic', 'TOP-02' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
