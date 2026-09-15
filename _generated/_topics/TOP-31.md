---
layout: hub
title: Study consistency
description: Studiare in modo discontinuo o senza una routine sostenibile.
permalink: /topics/study-consistency/
topic_id: TOP-31
---

# Study consistency

Studiare in modo discontinuo o senza una routine sostenibile.

{% assign items = site.data.content.content | where: 'topic', 'TOP-31' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
