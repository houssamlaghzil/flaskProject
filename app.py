from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def __page1__():
    return render_template("page.html")


@app.route('/donner2018.html')
def __page2__():
    return render_template("donner2018.html")


if __name__ == '__main__':
    app.run()
