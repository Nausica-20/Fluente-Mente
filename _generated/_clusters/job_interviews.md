---
layout: hub
title: job_interviews
description: Gestire le principali interazioni linguistiche durante un colloquio.
permalink: /english_for_real_life/job_interviews/
domain: english_for_real_life
cluster: job_interviews
---

# job_interviews

Gestire le principali interazioni linguistiche durante un colloquio.

{% assign items = site.data.content.content | where: 'cluster', 'job_interviews' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
