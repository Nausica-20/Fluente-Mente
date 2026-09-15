---
layout: hub
title: everyday_expressions
description: Comprendere espressioni e reazioni frequenti nella conversazione.
permalink: /understand_real_english/everyday_expressions/
domain: understand_real_english
cluster: everyday_expressions
---

# everyday_expressions

Comprendere espressioni e reazioni frequenti nella conversazione.

{% assign items = site.data.content.content | where: 'cluster', 'everyday_expressions' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
