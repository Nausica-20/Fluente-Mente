---
layout: hub
title: Job interview communication
description: Non sapere come parlare di sé e della propria esperienza in un colloquio.
permalink: /topics/job-interview-communication/
topic_id: TOP-21
---

# Job interview communication

Non sapere come parlare di sé e della propria esperienza in un colloquio.

{% assign items = site.data.content.content | where: 'topic', 'TOP-21' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
