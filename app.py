from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/payphone")
def payphone():
    return render_template("payphone.html")


@app.route("/mailbox")
def mailbox():
    return render_template("mailbox.html")


@app.route("/weather")
def weather():
    return render_template("weather.html")


if __name__ == "__main__":
    app.run(debug=True)
