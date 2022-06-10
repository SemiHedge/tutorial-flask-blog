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

### register.html
```html
{% extends "base.html" %} 
{% block title %}Register{% endblock %} 

{% block content%}
   
{% endblock %}
```

### login.html
```html
{% extends "base.html" %} 
{% block title %}Login{% endblock %} 

{% block content%}
   
{% endblock %}
```