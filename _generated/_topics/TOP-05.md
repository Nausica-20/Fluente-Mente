---
layout: hub
title: Clarifying and repairing communication
description: Non sapere cosa dire quando non si capisce qualcosa.
permalink: /topics/clarifying-and-repairing-communication/
topic_id: TOP-05
---

# Clarifying and repairing communication

Non sapere cosa dire quando non si capisce qualcosa.

{% assign items = site.data.content.content | where: 'topic', 'TOP-05' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
