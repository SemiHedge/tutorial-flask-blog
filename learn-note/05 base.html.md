# 목차
- `base.html`의 block 생성
- 상세 페이지에 extends 적용

## `base.html`의 block 생성
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

    {% block content %}
    
    {% endblock %}
</body>
</html>
```

## 상세 페이지에 extends 적용
### home.html
```html
{% extends "base.html" %} 
{% block title %}Home{% endblock %} 

{% block content%}
   
{% endblock %}
```

### sign_up.html
```html
{% extends "base.html" %} 
{% block title %}Sign Up{% endblock %} 

{% block content%}
   
{% endblock %}
```

### sign_in.html
```html
{% extends "base.html" %} 
{% block title %}Sign In{% endblock %} 

{% block content%}
   
{% endblock %}
```