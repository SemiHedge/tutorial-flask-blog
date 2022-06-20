from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

# define auth view
@auth.route("/sign-in", methods=['GET','POST'])
def sign_in():
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


@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        # 추출 - 회원 가입 요청 데이터
        email = request.form.get("email")
        nickname = request.form.get("nickname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # 조회 - 데이터베이스 User정보
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
            return redirect(url_for('auth.sign_in'))
    
    return render_template("sign_up.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.sign_in"))
