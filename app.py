import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/donner2018.html')
def __page1__():
    return render_template("donner2018.html")


@app.route('/donner sec.html')
def __page2__():
    return render_template("donner sec.html")


if __name__ == '__main__':
    app.run()
