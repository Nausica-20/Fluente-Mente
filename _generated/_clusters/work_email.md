---
layout: hub
title: work_email
description: Scrivere email professionali semplici, chiare e naturali.
permalink: /english_for_real_life/work_email/
domain: english_for_real_life
cluster: work_email
---

# work_email

Scrivere email professionali semplici, chiare e naturali.

{% assign items = site.data.content.content | where: 'cluster', 'work_email' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
