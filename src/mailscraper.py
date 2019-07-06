from bs4 import BeautifulSoup
import requests


def get_mail():
    URL = "https://temp-mail.org/de/" # todo sachen für github entfernen
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}
    page = requests.get(URL, headers)
    bs = BeautifulSoup(page.content, "html.parser")
    mail = bs.find(id="mail")

    return mail["value"]