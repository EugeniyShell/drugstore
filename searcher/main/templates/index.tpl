{% extends "base.html" %}

{% block content %}
    {% if message == "search"%}
        <h1>Welcome and {{ message }}</h1>
    {% else %}
        <h1>{{ message }}</h1>
    {% endif %}
    
    <form action="/result" method="GET">
        <fieldset>
            <legend>Введите название лекарства или действующего вещества:</legend>
            <input type="text" name="search">
        </fieldset>
        
        <button type="submit">Искать</button>
    </form>
{% endblock %}