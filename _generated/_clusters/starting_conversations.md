---
layout: hub
title: starting_conversations
description: Iniziare una conversazione in modo naturale.
permalink: /use_english/starting_conversations/
domain: use_english
cluster: starting_conversations
---

# starting_conversations

Iniziare una conversazione in modo naturale.

{% assign items = site.data.content.content | where: 'cluster', 'starting_conversations' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
