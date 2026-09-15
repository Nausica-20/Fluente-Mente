---
layout: hub
title: grammar_in_context
description: Imparare la grammatica attraverso situazioni comunicative.
permalink: /build_better_english/grammar_in_context/
domain: build_better_english
cluster: grammar_in_context
---

# grammar_in_context

Imparare la grammatica attraverso situazioni comunicative.

{% assign items = site.data.content.content | where: 'cluster', 'grammar_in_context' %}
{% for item in items %}
### {{ item.title | default: item.user_job }}
{{ item.learning_outcome }}

{% endfor %}
