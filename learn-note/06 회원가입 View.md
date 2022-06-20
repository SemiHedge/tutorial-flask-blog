# 목차
- sign_up.html 기본 구현
- 회원가입의 로직 구현(분기) - `auth.py`
- 회원가입의 로직 구현(DB조회) - `auth.py`
- 회원가입의 로직 구현(유효성검사) - `auth.py`
- 회원가입의 로직 구현(코드 정리) - `auth.py`
- 직접 확인해보기

## sign_up.html 기본 구현
```html
{% extends "base.html" %} 
{% block title %}Sign Up{% endblock %} 

{% block content%}
<form method="post">
    <h3 align="center">회원가입</h3>
    <label for="email">이메일</label>
    <input type="email" name="email" id="email">
    <label for="nickname">닉네임</label>
    <input type="text" name="nickname" id="nickname">
    <label for="password">비밀번호</label>
    <input type="password" name="password1" id="password1">
    <label for="password">비밀번호 확인</label>
    <input type="password" name="password2" id="password2">
    <button type="submit">회원가입 제출</button>
</form> 
{% endblock %}
```

## 회원가입의 로직 구현(분기) - `auth.py`
```python
@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        # 추출 - 회원 가입 요청 데이터
        email = request.form.get("email")
        nickname = request.form.get("nickname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
    else:
        return render_template("sign_up.html")

```

## 회원가입의 로직 구현(DB조회) - `auth.py`
```python
@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        # 추출 - 회원 가입 요청 데이터
        email = request.form.get("email")
        nickname = request.form.get("nickname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # 조회 - 데이터 베이스 User정보
        email_exist = User.query.filter_by(email=email).first()
        nickname_exist = User.query.filter_by(nickname=nickname).first()
    else:
        return render_template("sign_up.html")

```

## 회원가입의 로직 구현(유효성검사) - `auth.py`
```python
@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        # 추출 - 회원 가입 요청 데이터
        email = request.form.get("email")
        nickname = request.form.get("nickname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # 조회 - 데이터 베이스 User정보
        email_exist = User.query.filter_by(email=email).first()
        nickname_exist = User.query.filter_by(nickname=nickname).first()

        # 유효성 검사
        if email_exist:
            flash('이미 가입된 이메일입니다.', category='error')
            return render_template("sign_up.html")
        elif nickname_exist:
            flash('이미 존재하는 닉네임입니다.', category='error')
            return render_template("sign_up.html")
        elif len(nickname) < 2:
            flash('닉네임은 2글자부터입니다', category='error')
            return render_template("sign_up.html")
        elif password1 != password2:
            flash('비밀번호가 일치하지 않습니다', category='error')
            return render_template("sign_up.html")
        elif len(password1) < 8:
            flash('패스워드가 너무 짧습니다. 8자 이상', category='error')
            return render_template("sign_up.html")
        elif len(email) < 5:
            flash("올바른 이메일 정보를 입력하세요", category='error')
            return render_template("sign_up.html")
        else:
            new_user = User(email=email, nickname=nickname, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('회원 가입 성공')
            return redirect(url_for('auth.sign-in'))
    else:
        return render_template("sign_up.html")

```

## 회원가입의 로직 구현(코드 정리) - `auth.py`
- 유효성 검사의 `return render_template("sign_up.html")`가 너무 많습니다.
- 1차 : 회원가입처리하는 `else` 바깥에 옮깁니다.
- 2차 : POST, GET 둘 다 `return render_template("sign_up.html")`하네요. 합칩시다.
```python
@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        # 추출 - 회원 가입 요청 데이터
        email = request.form.get("email")
        nickname = request.form.get("nickname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # 조회 - 데이터 베이스 User정보
        email_exist = User.query.filter_by(email=email).first()
        nickname_exist = User.query.filter_by(nickname=nickname).first()

        # 유효성 검사
        if email_exist:
            flash('이미 가입된 이메일입니다.', category='error')
        elif nickname_exist:
            flash('이미 존재하는 닉네임입니다.', category='error')
        elif len(nickname) < 2:
            flash('닉네임은 2글자부터입니다', category='error')
        elif password1 != password2:
            flash('비밀번호가 일치하지 않습니다', category='error')
        elif len(password1) < 8:
            flash('패스워드가 너무 짧습니다. 8자 이상', category='error')
        elif len(email) < 5:
            flash("올바른 이메일 정보를 입력하세요", category='error')
        else:
            new_user = User(email=email, nickname=nickname, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('회원 가입 성공')
            return redirect(url_for('auth.signin'))
    
    return render_template("sign_up.html")
```

## 직접 확인해보기
- `flash`는 아직 jinja template을 작성 안해서 적용이 안됩니다.
- `database.db`를 열어 데이터 생성을 확인합시다.