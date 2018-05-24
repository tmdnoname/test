# _*_ coding:utf-8 _*_
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    print("joy改了")
    return "index"


if __name__ == "__main__":
    app.run(debug=True)
