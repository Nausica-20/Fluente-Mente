---
layout: hub
title: everyday_problem_solving
description: Gestire problemi, errori e richieste di soluzione nella vita quotidiana.
permalink: /english_for_real_life/everyday_problem_solving/
domain: english_for_real_life
cluster: everyday_problem_solving
---

# everyday_problem_solving

Gestire problemi, errori e richieste di soluzione nella vita quotidiana.

{% assign items = site.data.content.content | where: 'cluster', 'everyday_problem_solving' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
