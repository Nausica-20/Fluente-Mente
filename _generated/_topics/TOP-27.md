---
layout: hub
title: Speaking confidence
description: Paura di sbagliare o di essere giudicati mentre si parla.
permalink: /topics/speaking-confidence/
topic_id: TOP-27
---

# Speaking confidence

Paura di sbagliare o di essere giudicati mentre si parla.

{% assign items = site.data.content.content | where: 'topic', 'TOP-27' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
