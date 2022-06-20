# 목차
- 로그인 여부에 따른 Jinja 표현식 - `base.html`
- 직접 해보기

## 로그인 여부에 따른 Jinja 표현식 - `base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <!-- navbar가 될 영역 -->
    
    <!-- 공통 노출 -->
    <a href="/home">Home</a>
    {% if user.is_authenticated %}
        <!-- 로그인 시 노출 -->
        <a href="/logout">Logout</a>
    {% else %}
        <!-- 비로그인 시 노출 -->
        <a href="/sign-in">Sign In</a>
        <a href="/sign-up">Sign Up</a>
    {% endif %}

    <!-- flash 메세지 노출 -->
    {% with messages = get_flashed_messages(with_categories=True) %}
      {% if messages %}
        {% for category, message in messages %}
            {% if category == "error" %}
                {{ message }}
            {% else %}
                {{ message }}
            {% endif %}
        {% endfor %}
      {% endif %}
    {% endwith %}

    <!-- 페이지별 본문 영역 -->
    {% block content %}
    
    {% endblock %}
</body>
</html>
```

## 직접 해보기