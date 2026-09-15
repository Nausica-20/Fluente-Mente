---
layout: hub
title: Phone and video calls
description: Gestire conversazioni telefoniche o video senza il supporto delle espressioni
  facciali.
permalink: /topics/phone-and-video-calls/
topic_id: TOP-23
---

# Phone and video calls

Gestire conversazioni telefoniche o video senza il supporto delle espressioni facciali.

{% assign items = site.data.content.content | where: 'topic', 'TOP-23' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
