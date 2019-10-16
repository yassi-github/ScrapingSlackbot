from plugins.scripts.confirm_ad import Confirmad
from slackbot.bot import default_reply
from slackbot.bot import respond_to
import json
import pya3rt
import settings

@default_reply()
def send_message(message):
    APY = settings.APY
    client = pya3rt.TalkClient(APY)
    reply_message = client.talk(message.body['text'])
    message.reply(reply_message['results'][0]['reply'])

@respond_to('help')
def reply_help(message):
    attachments = [
        {
            'color': "#696969",
            'fields': [
                {'title': "コマンド", 'value': "help", 'short': True},
                {'title': "説明", 'value': "ヘルプを表示します", 'short': True},
                {'value': "granderies", 'short': True},
                {'value': "グランデリーズの広告をとってきます", 'short': True},
                {'value': "coop", 'short': True},
                {'value': "コープの広告をとってきます", 'short': True},
                {'value': "marunaka", 'short': True},
                {'value': "マルナカの広告をとってきます", 'short': True},
                {'value': "M, T, W, Th, F + 1~5", 'short': True},
                {'value': "曜日の頭文字と時間で、その授業の場所を教えてくれます。例:W3", 'short': True},
                {'value': "http [URL]", 'short': True},
                {'value': "任意のURLを入力すると、規定ブラウザで開くURLを返してくれます。LINE等で専用ブラウザを使わせたくないときに。", 'short': True},
            ],
            "footer": "自由に打ち込むことで軽い会話をしてくれます"
        }
    ]
    message.send_webapi('コマンド一覧', json.dumps(attachments))

@respond_to('http (.*)')
def reply_hello(message, arg):
    s = "?openExternalBrowser=1&"
    index_q = arg.find("?")
    index_h = arg.find("#")
    if index_h == index_q: arg = arg + "?"# 両方ないとき
    elif index_q == -1: arg = arg.replace("#", "?#")# #だけあるとき
    msg = arg.replace("?", s)
    message.reply(msg)

@respond_to("marunaka")
def reply_m(message):
    ad_m = Confirmad()
    ad_m.scraping1(message)

@respond_to("granderies")
def reply_g(message):
    ad_g = Confirmad()
    ad_g.scraping2(message)

@respond_to("coop")
def reply_c(message):
    ad_c = Confirmad()
    ad_c.scraping3(message)

@respond_to('(M|T|W|Th|F)([0-5])')
def reply_class(ins, message, times):
    # 時間割を直接書き込んでいる．
    if message == "M":
        if times == "1":place = "114"
        if times == "2":place = "5号館14講義室"
        if times == "3":place = ""
        if times == "4":place = ""
        if times == "5":place = ""
        if times == "0":place = "1:114\n2:5号館14講義室\n3:\n4:\n5:"
    if message == "T":
        if times == "1":place = "401"
        if times == "2":place = "58講義室"
        if times == "3":place = "19講義室"
        if times == "4":place = "168"
        if times == "5":place = "8棟図書室"
        if times == "0":place = "1:401\n2:58\n3:19\n4:168\n5:8棟図書室"

    if message == "W":
        if times == "1":place = "173"
        if times == "2":place = ""
        if times == "3":place = ""
        if times == "4":place = "049"
        if times == "5":place = "096"
        if times == "0":place = "1:\n2:\n3:\n4:3101\n5:"

    if message == "Th":
        if times == "1":place = ""
        if times == "2":place = ""
        if times == "3":place = ""
        if times == "4":place = "634"
        if times == "5":place = "546"
        if times == "0":place = "1:\n2:\n3:\n4:634\n5:546"

    if message == "F":
        if times == "1":place = ""
        if times == "2":place = "3014"
        if times == "3":place = ""
        if times == "4":place = "1592"
        if times == "5":place = "6535"
        if times == "0":place = "1:\n2:3014\n3:\n4:1592\n5:6535"

    ins.reply(place)

