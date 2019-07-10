from flask import Flask, render_template, request
import random
import string
from src.mailscraper import get_mail
from src.pricescraper import to_json, get_price, check_price, update_price
import json
app = Flask(__name__)

lower = string.ascii_lowercase
upper = string.ascii_uppercase
punc = string.punctuation
digits = string.digits


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate")
def generate():
    return render_template("generator.html")


@app.route("/generate/new", methods=["POST"])
def password():
    return render_template("generator.html", password=generate_pw(), mail=get_mail())
# utility website - pw generator, amazon proize tracker: mit discord verbinden

@app.route("/amazon")
def amazon():
    #check_price()
    update_price()
    with open("./src/articles.json") as fp:
        t = json.load(fp)
    check_price()
    return render_template("amazon.html", items=t)


@app.route("/amazon", methods=["POST"])
def get():
    url = request.form["url"]
    price = request.form["price"]
    name = request.form["name"]
    to_json(name, url, price)
    with open("./src/articles.json") as fp:
        t = json.load(fp)
    #check_price()
    return render_template("amazon.html", items=t)

def generate_pw():
    char = lower + upper + punc + digits
    password = "".join(random.choice(char) for x in range(random.randint(8, 16)))
    return password


app.run(debug=True, port=8080)