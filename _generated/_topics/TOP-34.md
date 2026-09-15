---
layout: hub
title: Choosing a language app
description: Faticare a distinguere un'app utile da una scelta basata solo su funzionalità
  o marketing.
permalink: /topics/choosing-a-language-app/
topic_id: TOP-34
---

# Choosing a language app

Faticare a distinguere un'app utile da una scelta basata solo su funzionalità o marketing.

{% assign items = site.data.content.content | where: 'topic', 'TOP-34' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
