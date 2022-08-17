{% extends "base.html" %}

{% block content %}
    <h1>
        Вы искали {% for item in search_list %}
            "{{ item }}"{% if not loop.last %}, {% endif %}
        {% endfor %}.
    </h1>

    <ul class="list-group">
        {% if result_list|length %}
            <li class="list-group-item">
                <h2>Нам удалось найти:</h2>
            </li>

            {% for item in result_list %}
                <li class="list-group-item">{{ item }}</li>
            {% endfor %}
        {% else %}
            <li class="list-group-item">
                <h2>Нам ничего не удалось найти.</h2>
            </li>
        {% endif %}
    </ul>
{% endblock %}