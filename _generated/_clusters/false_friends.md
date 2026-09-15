---
layout: hub
title: false_friends
description: Evitare falsi amici e parole ingannevoli per italiani.
permalink: /understand_real_english/false_friends/
domain: understand_real_english
cluster: false_friends
---

# false_friends

Evitare falsi amici e parole ingannevoli per italiani.

{% assign items = site.data.content.content | where: 'cluster', 'false_friends' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
