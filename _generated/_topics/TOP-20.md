---
layout: hub
title: Participating in meetings
description: Comprendere e intervenire nelle riunioni senza perdere il turno o risultare
  bruschi.
permalink: /topics/participating-in-meetings/
topic_id: TOP-20
---

# Participating in meetings

Comprendere e intervenire nelle riunioni senza perdere il turno o risultare bruschi.

{% assign items = site.data.content.content | where: 'topic', 'TOP-20' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
