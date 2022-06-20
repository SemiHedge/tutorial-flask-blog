from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

# define auth view
@auth.route("/sign-in")
def login():
    return render_template("sign_in.html")


@auth.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")


@auth.route("/logout")
def logout():
    return redirect(url_for("views.home"))