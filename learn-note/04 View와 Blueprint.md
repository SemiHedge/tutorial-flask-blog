# 목차
- `views.py`에 Blueprint 생성
- `auth.py`에 Blueprint 생성
- `__init__.py`에 Blueprint를 적용

## `views.py`에 Blueprint 생성
```python
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Post, User, Comment, Like
from . import db

views = Blueprint("views", __name__)
```

## `auth.py`에 Blueprint 생성
```python
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)
```


## `__init__.py`에 Blueprint를 적용
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

# Define Create Flask App
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

    return app


# Create DB when database does not exist
def create_database(app):
    if not path.exists("blog/" + DB_NAME):
        db.create_all(app = app)
        print(">>> Created DB ")
```