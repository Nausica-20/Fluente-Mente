---
layout: hub
title: Professional email communication
description: Scrivere email professionali troppo lunghe, dirette o tradotte letteralmente.
permalink: /topics/professional-email-communication/
topic_id: TOP-19
---

# Professional email communication

Scrivere email professionali troppo lunghe, dirette o tradotte letteralmente.

{% assign items = site.data.content.content | where: 'topic', 'TOP-19' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
