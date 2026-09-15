---
layout: hub
title: Grammar through everyday use
description: Conoscere le regole ma non sapere quando usarle mentre si parla.
permalink: /topics/grammar-through-everyday-use/
topic_id: TOP-12
---

# Grammar through everyday use

Conoscere le regole ma non sapere quando usarle mentre si parla.

{% assign items = site.data.content.content | where: 'topic', 'TOP-12' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
