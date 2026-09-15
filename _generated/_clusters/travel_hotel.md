---
layout: hub
title: travel_hotel
description: Comunicare efficacemente durante il soggiorno in hotel.
permalink: /english_for_real_life/travel_hotel/
domain: english_for_real_life
cluster: travel_hotel
---

# travel_hotel

Comunicare efficacemente durante il soggiorno in hotel.

{% assign items = site.data.content.content | where: 'cluster', 'travel_hotel' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
