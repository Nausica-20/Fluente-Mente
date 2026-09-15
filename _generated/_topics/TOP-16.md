---
layout: hub
title: Airport communication
description: Non sapere cosa dire o capire nei principali passaggi aeroportuali.
permalink: /topics/airport-communication/
topic_id: TOP-16
---

# Airport communication

Non sapere cosa dire o capire nei principali passaggi aeroportuali.

{% assign items = site.data.content.content | where: 'topic', 'TOP-16' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
