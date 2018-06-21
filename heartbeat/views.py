from flask import Blueprint

routes = Blueprint(r'routes', __name__) # pylint: disable=invalid-name

@routes.route('/')
def index():
    return 'Hello World!'
