---
layout: hub
title: Understanding spoken English
description: Capire poco l'inglese parlato nonostante una buona conoscenza grammaticale.
permalink: /topics/understanding-spoken-english/
topic_id: TOP-10
---

# Understanding spoken English

Capire poco l'inglese parlato nonostante una buona conoscenza grammaticale.

{% assign items = site.data.content.content | where: 'topic', 'TOP-10' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
