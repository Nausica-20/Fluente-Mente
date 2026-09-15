---
layout: hub
title: italian_mistakes
description: Individuare e correggere errori tipici degli italiani.
permalink: /build_better_english/italian_mistakes/
domain: build_better_english
cluster: italian_mistakes
---

# italian_mistakes

Individuare e correggere errori tipici degli italiani.

{% assign items = site.data.content.content | where: 'cluster', 'italian_mistakes' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
