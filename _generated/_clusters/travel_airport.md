---
layout: hub
title: travel_airport
description: Gestire comunicazioni essenziali in aeroporto.
permalink: /english_for_real_life/travel_airport/
domain: english_for_real_life
cluster: travel_airport
---

# travel_airport

Gestire comunicazioni essenziali in aeroporto.

{% assign items = site.data.content.content | where: 'cluster', 'travel_airport' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
