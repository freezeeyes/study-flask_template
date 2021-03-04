from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


# 非認証ルート
# **********************************************************************

# トップページ
@main.route('/')
def index():
    return render_template('index.html')


# マイページ
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
