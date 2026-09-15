---
layout: hub
title: Building speaking ability
description: Sapere che bisogna parlare ma non avere un sistema pratico per allenarsi.
permalink: /topics/building-speaking-ability/
topic_id: TOP-26
---

# Building speaking ability

Sapere che bisogna parlare ma non avere un sistema pratico per allenarsi.

{% assign items = site.data.content.content | where: 'topic', 'TOP-26' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
