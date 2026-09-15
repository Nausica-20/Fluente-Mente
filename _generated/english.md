---
layout: hub
title: Inglese pratico
description: Parlare e interagire in situazioni quotidiane.
permalink: /english/
domain: use_english
---

# Inglese pratico

Parlare e interagire in situazioni quotidiane.

{% assign items = site.data.content.content | where: 'domain', 'use_english' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
