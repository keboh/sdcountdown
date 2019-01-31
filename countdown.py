from flask import Flask, render_template
import datetime

# Set the time that you are going to arrive here.
# Go to https://www.epochconverter.com/ and punch in the date.
# Get the 'Epoch Timestamp' and plug it in.
TIME_EPOCH = 1551640988

app = Flask(__name__)


@app.route("/")
def index():
    date = datetime.datetime.fromtimestamp(TIME_EPOCH)
    return render_template("index.html", date=date)
