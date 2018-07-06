import os
from flask import Flask, Response


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)


app = Flask(__name__, static_url_path='/static')


@app.route("/")
def hello():
    content = get_file('view/index.html')
    return Response(content, mimetype="text/html")


app.run()
