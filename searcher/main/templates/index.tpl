{% extends "base.html" %}

{% block content %}
    {% if message == "search"%}
        <h1>Welcome and {{ message }}</h1>
    {% else %}
        <h1>{{ message }}</h1>
    {% endif %}
{% endblock %}