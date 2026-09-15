---
layout: hub
title: Hotel communication
description: Gestire check-in, richieste e problemi durante il soggiorno.
permalink: /topics/hotel-communication/
topic_id: TOP-17
---

# Hotel communication

Gestire check-in, richieste e problemi durante il soggiorno.

{% assign items = site.data.content.content | where: 'topic', 'TOP-17' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
