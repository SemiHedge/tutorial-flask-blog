# 목차
- flash 메세지 Jinja 표현식 - `base.html`
- 직접 해보기

## flash 메세지 Jinja 표현식 - `base.html`
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
    <a href="/home">Home</a>
    <a href="/sign-in">Sign In</a>
    <a href="/sign-up">Sign Up</a>

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
- 회원가입
    - 닉네임 1글자 해보기
    - 비밀번호 불일치 해보기
    - 기존 이메일로 가입해보기
    - 제대로 회원가입 해보기
- 로그인
    - 비밀번호 틀려보기
    - 이메일 틀려보기
    - 제대로 로그인 해보기
