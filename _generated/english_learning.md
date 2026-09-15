---
layout: hub
title: Sblocca il tuo inglese
description: Risolvere i problemi che bloccano l'apprendimento.
permalink: /english-learning/
domain: get_unstuck
---

# Sblocca il tuo inglese

Risolvere i problemi che bloccano l'apprendimento.

{% assign items = site.data.content.content | where: 'domain', 'get_unstuck' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
