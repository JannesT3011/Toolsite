from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", password=" dwadawd ")

app.run(debug=True, port=8080)