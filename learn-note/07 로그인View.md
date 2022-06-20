# 목차
- 플라스크 앱에 `login_manager` 붙이기
- 로그인 로직 구현(분기) 
- 로그인 로직 구현(DB조회) 
- 로그인 로직 구현(유효성검사)
- 직접 해보기 

## 플라스크 앱에 `login_manager` 붙이기
- [Flask-Login 세팅 가이드](https://flask-login.readthedocs.io/en/latest/#configuring-your-application)에 `.login_view`는 없지만, 로그인이 되어야만 접근 가능한 페이지를 구현하기 위해서 미리 해두자.

```python
def create_app():
    # Flask App Config
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "semicircle214"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import View
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Check DB exist & Create DB
    from .models import User, Post, Comment, Like
    create_database(app)

    # Config LoginManager
    login_manager = LoginManager()
    login_manager.login_view = "auth.sign-in"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    return app
```

## 로그인 로직 구현(분기) - `auth.py`
```python
@auth.route("/sign-in", methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        # 추출 - 회원 가입 요청 데이터
        email = request.form.get("email")
        password = request.form.get("password")
    
    return render_template("sign_in.html")
```

## 로그인 로직 구현(DB조회) - `auth.py`
- 회원가입시 조회코드와 동일합니다.
```python
@auth.route("/sign-in", methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        # 추출 - 회원 가입 요청 데이터
        email = request.form.get("email")
        password = request.form.get("password")

        # 조회 - 데이터베이스 User정보
        db_user = User.query.filter_by(email=email).first()
            
    return render_template("sign_in.html")
```

## 로그인 로직 구현(유효성검사) - `auth.py`
- 개인 취향인데, 회원가입에서도 유효성 검사시 `error`에 해당하는 부분을 위로 올렸으니, 여기서도 맞춰보았습니다.

```python
@auth.route("/sign-in", methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        # 추출 - 회원 가입 요청 데이터
        email = request.form.get("email")
        password = request.form.get("password")

        # 조회 - 데이터베이스 User정보
        db_user = User.query.filter_by(email=email).first()

        # 유효성 검사
        if not db_user:
            flash('이메일을 확인해주세요.', category='error')
        else:
            if not check_password_hash(db_user.password, password):
                flash('비밀번호를 확인해주세요.', category='error')
            else:
                flash(f"{db_user.nickname}님 반갑습니다", category='success')
                login_user(db_user, remember=True)
                return redirect(url_for('views.home'))
            
    return render_template("sign_in.html")
```

## 직접 해보기
- 로그인이 제대로 된다면 `home.html`로 이동될 것
- 안된다면 `sign_in.html`로 이동될 것