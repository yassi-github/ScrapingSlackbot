from bs4 import BeautifulSoup
from urllib import request
import re

class Confirmad():

    def __init__(self):
        pass

    def scraping1(self, message):
        url = "http://www.marunaka.net/tenpo/shikoku/chirashi_list_new.php?area=3"
        res = request.urlopen(url)
        soup = BeautifulSoup(res, features="html.parser")

        # ここでは宮脇店を探索．"宮脇"を任意のキーワードに置換して使用可．
        out = soup.find("a", string=re.compile("宮脇"))
        out_p = out.find_parent("div")
        out_p1 = out_p.find_parent("div")

        def findhtml(href):
            return href and re.compile("html").search(href)

        out_tp = out_p1.findAll(href=findhtml)
        for a in out_tp:
            if "href" in a.attrs:
                link = a.attrs["href"]
                ml = link[1:]
                ht = "http://www.marunaka.net/tenpo/shikoku"
                html = ht + ml
                message.send(html)

    def scraping2(self, message):
        # 昭和町店のURLを探索．任意のマルヨシセンターの店舗URL(末尾のidが違うだけ)に置換して使用可．
        url = "http://ww2.maruyoshi-center.co.jp/shop/detail.php?id=49"
        res = request.urlopen(url)
        soup = BeautifulSoup(res, features="html.parser")

        out = soup.find("a", id="bnrLeaflet")
        message.send(out["href"])

    def scraping3(self, message):
        url = "http://www.kagawa.coop.or.jp/shop/info/"
        res = request.urlopen(url)
        soup = BeautifulSoup(res, features="html.parser")

        out = soup.find("iframe")
        out_src = out.get("src")
        dom = request.urlopen(out_src)
        beautiful = BeautifulSoup(dom, features="html.parser")

        # ここでは扇町店を探索．"扇町"を任意のキーワードに置換して使用可．
        out_tirashi = beautiful.find_all("li", string=re.compile("扇町"))
        # 扇町という文字があれば広告画像全てをとってくる．
        if out_tirashi is not None: message.send(out_src)
