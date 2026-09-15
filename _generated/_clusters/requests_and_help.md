---
layout: hub
title: requests_and_help
description: Chiedere aiuto, fare richieste e gestire incomprensioni.
permalink: /use_english/requests_and_help/
domain: use_english
cluster: requests_and_help
---

# requests_and_help

Chiedere aiuto, fare richieste e gestire incomprensioni.

{% assign items = site.data.content.content | where: 'cluster', 'requests_and_help' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
