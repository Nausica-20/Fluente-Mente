---
layout: hub
title: False friends
description: Interpretare parole simili all'italiano nel modo sbagliato.
permalink: /topics/false-friends/
topic_id: TOP-11
---

# False friends

Interpretare parole simili all'italiano nel modo sbagliato.

{% assign items = site.data.content.content | where: 'topic', 'TOP-11' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
