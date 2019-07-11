import requests
from bs4 import BeautifulSoup
import json
from src import send_mail
from config import my_user_agent

def get_price(item_url:str):
    headers = {"User-Agent": my_user_agent}
    page = requests.get(item_url, headers=headers)
    bs = BeautifulSoup(page.content, "html.parser")
    price = bs.find(id="priceblock_ourprice").get_text()
    return price.split("€")[0][:-1]


def check_price():
    with open("./src/articles.json") as fp:
        items = json.load(fp)
    for i in items:
        if i["amazon_price"] <= i["price"]:
            send_mail(i)
            continue


def to_json(name:str, item_url:str, price:str):
    with open("./src/articles.json") as fp:
        data_list = json.load(fp)

    data = {}
    data["Name"] = name
    data["url"] = item_url
    data["price"] = price
    data["notify"] = "False"
    if not item_url is None:
        data["amazon_price"] = get_price(item_url)
    data_list.append(data)

    with open("./src/articles.json", "w") as fp:
        json.dump(data_list, fp, indent=2)


def update_price():
    with open("./src/articles.json") as fp:
        data_list = json.load(fp)
    NEW = []
    for dic in data_list:
        dic.update(amazon_price=get_price(dic["url"]))
        NEW.append(dic)
    with open("./src/articles.json", "w") as fp:
        json.dump(NEW, fp, indent=2)