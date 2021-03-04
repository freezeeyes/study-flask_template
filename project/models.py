from flask_login import UserMixin
from . import db


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
