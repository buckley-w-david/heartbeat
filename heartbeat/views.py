from flask import Blueprint
from heartbeat.counts import counter

routes = Blueprint(r"routes", __name__)  # pylint: disable=invalid-name


@routes.route("/")
def index():
    return "Hello World!"


@routes.route('/count/<page>')
def count(page):
    return counter.get(page)
