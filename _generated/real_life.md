---
layout: hub
title: English for real life
description: Usare l'inglese in viaggio, lavoro, vita sociale e problemi quotidiani.
permalink: /english-for-real-life/
domain: english_for_real_life
---

# English for real life

Usare l'inglese in viaggio, lavoro, vita sociale e problemi quotidiani.

{% assign items = site.data.content.content | where: 'domain', 'english_for_real_life' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
