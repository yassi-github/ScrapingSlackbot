# Scraping Slackbot

スクレイピング等の機能を持たせたSlack Bot

※ Talk API 関連はコメントアウトしています

Classic App を使っているので21年以降使えなくなる…？

herokuで使うことを想定しています

## Description

- `help` でコマンドの一覧を表示  
- `marunaka`，`coop`，`granderies` でそれぞれの広告を取得  
- `W` のように，曜日の頭文字で講義教室の表示  
- `http [URL]` のように入力したURLを、 LINEで開いたときに標準ブラウザで開くパラメータを付加
<!-- - コマンド以外で会話 -->

## Requirements

- [Slack bot API トークン](https://api.slack.com/)
<!-- - [A3RT Talk API](https://a3rt.recruit-tech.co.jp/product/talkAPI/) -->
<!-- - [Python 3.7](https://www.python.org/downloads/) -->

## Preparation

<!-- ```Python
pip install -r requirements.txt
``` -->
1. SlackBotを作成する
    1. [api.slack.com](https://api.slack.com/rtm#classic)からClassicAppをつくる(名前を決める)
    1. AppHome > Add Legacy Bot User で表示名とフルネームを設定
    1. OAuth & Permissions > Install App to Workspace でワークスペースにボットを追加
    <!-- 1. Copy Bot User OAuth Access Token & Paste .env > API_TOKEN -->
    <!-- 1. https://api.slack.com/methods/conversations.list/test を使ってAPIの動作を確認する。必要に応じてscopeを追加許可する。 -->
    1. Bot User OAuth Access Tokenをコピーしておく
1. 教室名を書き換える
    1. `.env.sample`の教室名の記述を書き換える(herokuを使わない場合はAPIトークンも書き換える)
    1. `.env.sample`を`.env`にリネームする
    1. `.gitignore`を消す
1. [heroku](https://jp.heroku.com/)にあげる
    1. `heroku create {アプリ名}`
    1. Buildpacks: python
    1. gitであげる。`heroku git:remote -a {アプリ名}`(リモートリポジトリに登録) `git init` `git add .` `git commit -m "comment"` `git push heroku master`
    1. Config Varsで `Key: API_TOKEN` `Value: コピーしておいたBot User OAuth Acess Token` を設定
    1. `heroku ps:scale worker=1 -a {herokuのアプリ名}` でアプリ起動

## Usage

DMかbotへのメンションで`help`と入力するとコマンドの使い方が表示される。  

広告とってくる機能は，`confirm_ad.py`を適当に書き換えて使用可。

<!-- 1. APIキーの発行
    1. Slackbot API の権限は，Admin, Interactivity.
    1. Bot User OAuth Acess Token を使用
1. `.env.sample` を `.env` にリネーム
    1. `.gitignore`を消す
    1. API_TOKEN に Slackbot のAPIキーを書き込む
    <!-- 1. API_TOKEN と  API_KEY にそれぞれ Slackbot と TalkAPI のAPIキーを書き込む
    1. 教室名を追記する -->
<!-- 1. Python3のインストール
    1. モジュールのインストールは [上記](#Installation) の通り -->
    
<!-- 1. `whereplace.py` の教室名や，`confirm_ad.py` のURL等を適宜書き換えてカスタマイズできる
1. `run.py` を実行すると，あなたの追加した Slack Bot とのやり取りが可能になる -->

<!-- - Procfile等もあるので，環境変数などの設定を行えば，herokuで動かすことも可能です -->

## LICENSE

[MIT License](./LICENSE)