"""MODULE DOCSTRING"""
import enum
import flask
from heartbeat import views
from heartbeat.sockets import socketio

__version__ = "0.1.0"


@enum.unique
class Environment(enum.Enum):
    """Definition of different deployment environments"""

    TESTING = enum.auto()
    DEVELOPMENT = enum.auto()
    PRODUCTION = enum.auto()

    @staticmethod
    def from_string(env: str) -> "Environment":
        return getattr(Environment, env)


CONFIGMAP = {
    Environment.TESTING: "heartbeat.config.TestingConfig",
    Environment.DEVELOPMENT: "heartbeat.config.DevelopmentConfig",
    Environment.PRODUCTION: "heartbeat.config.ProductionConfig",
}


def create_app(environment: Environment):
    """Create heartbeat flask app"""

    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_object(CONFIGMAP[environment])
    app.config.from_pyfile("application.cfg", silent=True)

    socketio.init_app(app)
    app.register_blueprint(views.routes, url_prefix=r"/")

    return app
