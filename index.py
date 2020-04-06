
from flask import request

from flask import Flask

app = Flask(__name__)


@app.route('/')
def __hello_world__():
    langage = request.args.get('langage')
    return "<h1> {} </h1>".format(langage)

