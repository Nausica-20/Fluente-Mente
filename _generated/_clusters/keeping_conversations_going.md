---
layout: hub
title: keeping_conversations_going
description: Mantenere, sviluppare e reindirizzare una conversazione.
permalink: /use_english/keeping_conversations_going/
domain: use_english
cluster: keeping_conversations_going
---

# keeping_conversations_going

Mantenere, sviluppare e reindirizzare una conversazione.

{% assign items = site.data.content.content | where: 'cluster', 'keeping_conversations_going' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
