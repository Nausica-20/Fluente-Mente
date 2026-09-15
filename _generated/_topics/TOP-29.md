---
layout: hub
title: Listening to native speakers
description: Comprendere esercizi e insegnanti ma faticare con parlanti naturali.
permalink: /topics/listening-to-native-speakers/
topic_id: TOP-29
---

# Listening to native speakers

Comprendere esercizi e insegnanti ma faticare con parlanti naturali.

{% assign items = site.data.content.content | where: 'topic', 'TOP-29' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
