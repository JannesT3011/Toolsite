from bs4 import BeautifulSoup
import requests
from config import my_user_agent


def get_mail():
    URL = "https://temp-mail.org/de/"
    headers = {"User-Agent": my_user_agent}
    page = requests.get(URL, headers)
    bs = BeautifulSoup(page.content, "html.parser")
    mail = bs.find(id="mail")

    return mail["value"]