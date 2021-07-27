# Django による select for update の実装サンプル

## 概要

Django アプリとそれをさっと動かすためのDocker構成の詰め合わせです。

### アプリ概要

チュートリアルの polls データベースを使って（ちょっと拡張して）います。

- polls に amount（数量）を追加
- 数量を足したり減らしたりする操作を追加
- 減らす方にロックをかける実装が埋まっています

### Dockerの構成

- web (Djangoコマンドラインで実行されたもの）: port 8000
- db (PostgreSQL) : port 5432
- adminer(PostgreSQLなどを操作するためのアプリ...Djangoのadminでもいいんですが） : port 8080


## 動かし方

### 最初は下記をやってください

まずサーバを起動して必要な設定を行います

```
$ git clone git@github.com:tetsunosuke/django_sample_app.git
$ cd django_sample_app
$ docker compose up -d
$ docker compose run web python manage.py migrate
```

ブラウザで http://localhost:8080 へ入り

- データベース種類をPostgreSQL
- ユーザ名: testuser
- パスワード: testpass
- データベース: testdb

としてログインします

画面左下 polls_question を選んで、中央付近 項目の作成 を選択します。

question_textに適当な文字列、 pub_dateはプルダウンからnowを選択、数量は適当に10と入れておきましょう。

これでアプリが使えるようになるので http://localhost:8000/polls を開きます

あとは `add 1`, `buy 1` などを実行すると商品数が増減します










