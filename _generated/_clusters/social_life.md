---
layout: hub
title: social_life
description: Usare l'inglese per creare e mantenere relazioni sociali.
permalink: /english_for_real_life/social_life/
domain: english_for_real_life
cluster: social_life
---

# social_life

Usare l'inglese per creare e mantenere relazioni sociali.

{% assign items = site.data.content.content | where: 'cluster', 'social_life' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
