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

    # Config LoginManager
    login_manager = LoginManager()
    login_manager.login_view = "auth.sign-in"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    return app


# Create DB when database does not exist
def create_database(app):
    if not path.exists("blog/" + DB_NAME):
        db.create_all(app = app)
        print(">>> Created DB ")