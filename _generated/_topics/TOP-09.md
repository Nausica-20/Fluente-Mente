---
layout: hub
title: Natural English for Italians
description: Produrre inglese corretto ma troppo letterale o influenzato dall'italiano.
permalink: /topics/natural-english-for-italians/
topic_id: TOP-09
---

# Natural English for Italians

Produrre inglese corretto ma troppo letterale o influenzato dall'italiano.

{% assign items = site.data.content.content | where: 'topic', 'TOP-09' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
