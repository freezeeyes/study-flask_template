from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


# 初期設定
# **********************************************************************

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hogehoge'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
# login_manager.init_app(app)


# モデルの定義（データベースのテーブル定義）
# **********************************************************************

class User(UserMixin, db.Model):
    '''
    Userモデルクラス（usersテーブル）
    '''

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(20))


# 関数の定義
# **********************************************************************

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# 非認証ルート
# **********************************************************************

# トップページ
@app.route('/')
def index():
    return render_template('index.html')


# マイページ
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


# 認証ルート
# **********************************************************************

# サインアップページ
@app.route('/signup')
def signup():
    return render_template('signup.html')


# サインアップ処理
@app.route('/signup', methods=['POST'])
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
        return redirect(url_for('signup'))
    
    # 新規アカウントを生成する
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # usersテーブルに新規アカウントを追加する
    db.session.add(new_user)
    db.session.commit()

    # ログインページに遷移する
    return redirect(url_for('login'))


# ログインページ
@app.route('/login')
def login():
    return render_template('login.html')


# ログイン処理
@app.route('/login', methods=['POST'])
def login_post():
    # ログインページの入力フォームの値を取得する
    password = request.form.get('password')
    email = request.form.get('email')
    remember = True if request.form.get('remember') else False

    # usersテーブルからemailでアカウント情報を取得する
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('メールアドレスまたはパスワードが間違っています。')
        return redirect(url_for('login'))

    # セッションにアカウントの認証情報を保存する
    login_user(user, remember=remember)
    # マイページに遷移する
    return redirect(url_for('profile'))


# ログアウト処理
@app.route('/logout')
@login_required
def logout():
    # セッションからアカウントの認証情報を削除する
    logout_user()
    # マイページに遷移する
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
