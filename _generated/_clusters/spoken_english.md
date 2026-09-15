---
layout: hub
title: spoken_english
description: Capire perché l'inglese parlato dai nativi può sembrare diverso o difficile.
permalink: /understand_real_english/spoken_english/
domain: understand_real_english
cluster: spoken_english
---

# spoken_english

Capire perché l'inglese parlato dai nativi può sembrare diverso o difficile.

{% assign items = site.data.content.content | where: 'cluster', 'spoken_english' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
