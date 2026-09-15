---
layout: hub
title: Collocations and natural word combinations
description: Conoscere le parole singolarmente ma combinarle in modo innaturale.
permalink: /topics/collocations-and-natural-word-combinations/
topic_id: TOP-15
---

# Collocations and natural word combinations

Conoscere le parole singolarmente ma combinarle in modo innaturale.

{% assign items = site.data.content.content | where: 'topic', 'TOP-15' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
