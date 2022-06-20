from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Post, User, Comment, Like
from . import db

views = Blueprint("views", __name__)

# Define View
@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html')