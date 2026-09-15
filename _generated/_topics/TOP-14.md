---
layout: hub
title: Italian-to-English interference
description: Trasferire struttura, ordine o scelta lessicale dall'italiano all'inglese.
permalink: /topics/italian-to-english-interference/
topic_id: TOP-14
---

# Italian-to-English interference

Trasferire struttura, ordine o scelta lessicale dall'italiano all'inglese.

{% assign items = site.data.content.content | where: 'topic', 'TOP-14' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
