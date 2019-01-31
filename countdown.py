from flask import Flask, render_template
import datetime
import os


TIME_EPOCH = int(os.getenv("TIME"))
MESSAGE = os.getenv("MESSAGE")

app = Flask(__name__)


@app.route("/")
def index():
    date = datetime.datetime.fromtimestamp(TIME_EPOCH - 21600)
    return render_template("index.html", date=date, message=MESSAGE)
