import flask , time

app = flask.Flask(__name__)


@app.route("/")
def index():
    test
    return "Welcome!!! ",time.localtime