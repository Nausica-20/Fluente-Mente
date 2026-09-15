---
layout: hub
title: Starting conversations naturally
description: Non sapere come iniziare una conversazione senza usare formule scolastiche.
permalink: /topics/starting-conversations-naturally/
topic_id: TOP-01
---

# Starting conversations naturally

Non sapere come iniziare una conversazione senza usare formule scolastiche.

{% assign items = site.data.content.content | where: 'topic', 'TOP-01' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
