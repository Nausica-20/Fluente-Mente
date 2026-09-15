---
layout: hub
title: Understanding Babbel
description: Non sapere come funziona Babbel o per chi può avere senso.
permalink: /topics/understanding-babbel/
topic_id: TOP-35
---

# Understanding Babbel

Non sapere come funziona Babbel o per chi può avere senso.

{% assign items = site.data.content.content | where: 'topic', 'TOP-35' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
