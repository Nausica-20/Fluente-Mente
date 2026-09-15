---
layout: hub
title: Deciding whether Babbel fits
description: Non sapere se Babbel sia adatto al proprio livello, obiettivo e modo
  di studiare.
permalink: /topics/deciding-whether-babbel-fits/
topic_id: TOP-36
---

# Deciding whether Babbel fits

Non sapere se Babbel sia adatto al proprio livello, obiettivo e modo di studiare.

{% assign items = site.data.content.content | where: 'topic', 'TOP-36' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
