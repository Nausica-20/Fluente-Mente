---
layout: hub
title: Everyday problem solving
description: Blocchi linguistici quando qualcosa va storto e bisogna chiedere una
  soluzione.
permalink: /topics/everyday-problem-solving/
topic_id: TOP-24
---

# Everyday problem solving

Blocchi linguistici quando qualcosa va storto e bisogna chiedere una soluzione.

{% assign items = site.data.content.content | where: 'topic', 'TOP-24' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
