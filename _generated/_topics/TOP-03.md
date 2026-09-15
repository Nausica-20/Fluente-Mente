---
layout: hub
title: Keeping a conversation going
description: Rimanere senza parole dopo le prime battute.
permalink: /topics/keeping-a-conversation-going/
topic_id: TOP-03
---

# Keeping a conversation going

Rimanere senza parole dopo le prime battute.

{% assign items = site.data.content.content | where: 'topic', 'TOP-03' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
