from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User


auth = Blueprint('auth', __name__)


# 認証ルート
# **********************************************************************

# サインアップページ
@auth.route('/signup')
def signup():
    return render_template('signup.html')


# サインアップ処理
@auth.route('/signup', methods=['POST'])
def signup_post():
    # サインアップページの入力フォームの値を取得する
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # usersテーブルからemailでアカウント情報を取得する
    user = User.query.filter_by(email=email).first()

    # 既にアカウント情報がある場合はサインアップページに遷移する
    if user:
        flash('既にメールアドレスが登録されています。')
        return redirect(url_for('auth.signup'))
    
    # 新規アカウントを生成する
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # usersテーブルに新規アカウントを追加する
    db.session.add(new_user)
    db.session.commit()

    # ログインページに遷移する
    return redirect(url_for('auth.login'))


# ログインページ
@auth.route('/login')
def login():
    return render_template('login.html')


# ログイン処理
@auth.route('/login', methods=['POST'])
def login_post():
    # ログインページの入力フォームの値を取得する
    password = request.form.get('password')
    email = request.form.get('email')
    remember = True if request.form.get('remember') else False

    # usersテーブルからemailでアカウント情報を取得する
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('メールアドレスまたはパスワードが間違っています。')
        return redirect(url_for('auth.login'))

    # セッションにアカウントの認証情報を保存する
    login_user(user, remember=remember)
    # マイページに遷移する
    return redirect(url_for('profile'))


# ログアウト処理
@auth.route('/logout')
@login_required
def logout():
    # セッションからアカウントの認証情報を削除する
    logout_user()
    # マイページに遷移する
    return redirect(url_for('index'))
