{% extends "base.html" %}

{% block content %}
    <h1>"Вы искали "{{ message }}"</h1>

    <form action="/result" method="POST">
        <fieldset>
            <legend>Выберите вариант</legend>

            {% for item in search_list %}
                <label>
                    {{ item }}
                    <input type="radio" name="search" value="{{ item }}">
                </label><br>
            {% endfor %}
        </fieldset>
        
        <button type="submit">Искать</button>
    </form>
{% endblock %}