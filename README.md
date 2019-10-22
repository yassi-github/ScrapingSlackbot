# Scraping Slackbot

スクレイピング等の機能を持たせたSlack Bot

## Description

- `help` でコマンドの一覧を表示  
- `marunaka`，`coop`，`granderies` でそれぞれの広告を取得  
- `W` のように，曜日の頭文字で講義教室の表示  
- `http [URL]` で入力したURLを標準ブラウザで開くパラメータを付加
- コマンド以外で会話

## Requirements

- [Slack bot API](https://api.slack.com/)
- [A3RT Talk API](https://a3rt.recruit-tech.co.jp/product/talkAPI/)
- [Python 3.7](https://www.python.org/downloads/)

## Installation

```Python
pip install -r requirements.txt
```

## Usage

1. APIキーの発行
    1. Slackbot API の権限は，Admin, Interactivity.
    1. Bot User OAuth Acess Token を使用
1. `.env.sample` を `.env` にリネームし， API_TOKEN と  API_KEY にそれぞれ Slackbot と TalkAPI のAPIキーを書き込む
1. Python3のインストール
    1. モジュールのインストールは [上記](#Installation) の通り
1. `confirm_ad.py` のURLとキーワード，`whereplace.py` の教室名を適宜書き換えてカスタマイズできる
1. `run.py` を実行すると，あなたの追加した Slack Bot とのやり取りが可能になる

## LICENSE

[MIT License](./LICENSE)