---
layout: hub
title: Requests and help
description: Chiedere qualcosa o chiedere aiuto senza risultare bruschi o poco chiari.
permalink: /topics/requests-and-help/
topic_id: TOP-04
---

# Requests and help

Chiedere qualcosa o chiedere aiuto senza risultare bruschi o poco chiari.

{% assign items = site.data.content.content | where: 'topic', 'TOP-04' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
