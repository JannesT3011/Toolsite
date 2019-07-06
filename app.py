from flask import Flask, render_template
import random
import string
from src.mailscraper import get_mail
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

@app.route("/buy")
def buy():
    return "test"

def generate_pw():
    char = lower + upper + punc + digits
    password = "".join(random.choice(char) for x in range(random.randint(8, 16)))
    return password


app.run(debug=True, port=8080)