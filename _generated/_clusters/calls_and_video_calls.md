---
layout: hub
title: calls_and_video_calls
description: Gestire conversazioni telefoniche e videochiamate in inglese.
permalink: /english_for_real_life/calls_and_video_calls/
domain: english_for_real_life
cluster: calls_and_video_calls
---

# calls_and_video_calls

Gestire conversazioni telefoniche e videochiamate in inglese.

{% assign items = site.data.content.content | where: 'cluster', 'calls_and_video_calls' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
