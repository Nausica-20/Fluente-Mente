---
layout: hub
title: collocations
description: Passare dalle singole parole alle combinazioni naturali di parole.
permalink: /build_better_english/collocations/
domain: build_better_english
cluster: collocations
---

# collocations

Passare dalle singole parole alle combinazioni naturali di parole.

{% assign items = site.data.content.content | where: 'cluster', 'collocations' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
