from plugins.scripts.confirm_ad import ConfirmAD
from slackbot.bot import default_reply
from slackbot.bot import respond_to
import json
# import pya3rt
import settings


# @default_reply()
# def send_message(message):
#     APY = settings.APY
#     client = pya3rt.TalkClient(APY)
#     reply_message = client.talk(message.body['text'])
#     message.reply(reply_message['results'][0]['reply'])

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
                {'value': "M, T, W, Th, F", 'short': True},
                {'value': "曜日の頭文字で、その日の授業の場所を教えてくれます。例:W", 'short': True},
                {'value': "http [URL]", 'short': True},
                {'value': "任意のURLを入力すると、LINEにて規定ブラウザで開くURLを返してくれます。", 'short': True},
            ],
            # "footer": "自由に打ち込むことで軽い会話をしてくれます"
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
    ad_m = ConfirmAD()
    ad_m.scraping_m(message)

@respond_to("granderies")
def reply_g(message):
    ad_g = ConfirmAD()
    ad_g.scraping_g(message)

@respond_to("coop")
def reply_c(message):
    ad_c = ConfirmAD()
    ad_c.scraping_c(message)

@respond_to('(M|T|W|Th|F)')
def reply_class(ins, message):
    # 時間割を直接書き込んでいる．
    if message == "M":
        place_m = settings.place_m
        place = place_m

    if message == "T":
        place_t = settings.place_t
        place = place_t

    if message == "W":
        place_w = settings.place_w
        place = place_w

    if message == "Th":
        place_th = settings.place_th
        place = place_th

    if message == "F":
        place_f = settings.place_f
        place = place_f

    ins.reply(place)

