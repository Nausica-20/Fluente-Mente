---
layout: hub
title: Choosing a learning method
description: Non sapere quale combinazione di corso, tutor, app o self-study sia adatta.
permalink: /topics/choosing-a-learning-method/
topic_id: TOP-33
---

# Choosing a learning method

Non sapere quale combinazione di corso, tutor, app o self-study sia adatta.

{% assign items = site.data.content.content | where: 'topic', 'TOP-33' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
