from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user


# 初期設定
# **********************************************************************

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hogehoge'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
# login_manager.init_app(app)


# モデルクラスの読み込み
# **********************************************************************

from .models import User


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


# 認証ルートの読み込み
# **********************************************************************

# 認証機能のルートをプロジェクトに登録する
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
