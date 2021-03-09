# study-flask_template

このプロジェクトは、Flask学習用で、既にログイン機能が実装されています。
Flaskでウェブアプリケーションを作成する際は、このリポジトリをコピーすることで、開発者はメイン部分の実装に集中することができます。

データベースはSQLiteを使用しています。


# 開発環境の構築手順

1. GitHubに新しいリポジトリを作成する

2. ローカル環境にリポジトリのベアクローンを作成する

```
$ git clone --bare https://github.com/freezeeyes/study-flask_template.git
```

3. 新しいリポジトリにミラープッシュする

```
$ cd study-flask_template.git
$ git push --mirror https://github.com/ユーザ名/リポジトリ名.git
```

4. ローカル環境にあるベアクローンしたリポジトリを削除する

```
$ cd ../
$ rm -rf study-flask_template.git
```

5. 新しいリポジトリをクローンする

```
$ git clone https://github.com/ユーザ名/リポジトリ名.git
```

以降のプッシュは、１で作成した新しいリポジトリに反映される。
プロジェクトテンプレートには反映されない。


## パッケージのインストール

```
$ pip3 install flask flask-sqlalchemy flask-login
```

## データベースファイルの生成

以下のコマンドを実行するとprojectディレクトリ内にデータベースファイルが生成されます。データベースのテーブル構成の変更には対応していません。テーブル構成を変更する際は、データベースファイルを再度生成してください。

```
$ python3
>>> from app import db
>>> db.create_all()
```

## 起動方法

### Windows10

PowerShellの場合

```
$ $env:FLASK_APP="project"
$ $env:FLASK_DEBUG=1
```


CMDの場合

```
$ set FLASK_APP=project
$ set FLASK_DEBUG=1
```

### Linux

```
$ export FLASK_APP=project
$ export FLASK_DEBUG=1
$ python3 -m flask run
```


# 参考にしたウェブサイト

- [Flask-Login を使用してアプリケーションに認証を追加する方法](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login-ja)
- [【保存版】Python(Flask)×Webアプリ開発入門コース【1時間でOK！】](https://www.youtube.com/watch?v=jP7p2okKdJA)
- [Welcome to Flask — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/)
