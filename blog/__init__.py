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

    # Check DB exist
    create_database(app)

    return app


# Create DB when database does not exist
def create_database(app):
    if not path.exists("blog/" + DB_NAME):
        db.create_all(app = app)
        print(">>> Created DB ")