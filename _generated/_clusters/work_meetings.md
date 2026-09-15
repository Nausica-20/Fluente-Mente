---
layout: hub
title: work_meetings
description: Partecipare attivamente a riunioni in inglese.
permalink: /english_for_real_life/work_meetings/
domain: english_for_real_life
cluster: work_meetings
---

# work_meetings

Partecipare attivamente a riunioni in inglese.

{% assign items = site.data.content.content | where: 'cluster', 'work_meetings' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
