from flask import Flask, render_template
import random
import string

app = Flask(__name__)

lower = string.ascii_lowercase
upper = string.ascii_uppercase
punc = string.punctuation
digits = string.digits

@app.route("/")
def index():
    return render_template("index.html", password=generate_pw())


def generate_pw():
    char = lower + upper + punc + digits
    password = "".join(random.choice(char) for x in range(random.randint(8, 16)))
    return password


app.run(debug=True, port=8080)