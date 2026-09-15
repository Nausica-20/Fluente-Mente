---
layout: hub
title: Understand but cannot speak
description: Capire l'inglese ma non riuscire a trasformare la conoscenza in produzione.
permalink: /topics/understand-but-cannot-speak/
topic_id: TOP-25
---

# Understand but cannot speak

Capire l'inglese ma non riuscire a trasformare la conoscenza in produzione.

{% assign items = site.data.content.content | where: 'topic', 'TOP-25' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
