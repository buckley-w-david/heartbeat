import typing
from flask import current_app, _app_ctx_stack
import redis

class PageCounter(object):

    def __init__(self, app=None) -> None:
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app) -> None:
        app.config.setdefault('REDIS_HOST', 'localhost')
        app.config.setdefault('REDIS_PORT', '63790')
        app.config.setdefault('REDIS_DB', '0')

        app.teardown_appcontext(self.teardown)


    def connect(self) -> redis.StrictRedis:
        return redis.StrictRedis(
            host=current_app.config['REDIS_HOST'],
            port=current_app.config['REDIS_PORT'],
            db=current_app.config['REDIS_DB'],
        )

    def teardown(self, exception) -> None:
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'redis_db'):
            ctx.redis_db.close()

    @property
    def connection(self) -> redis.StrictRedis:
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'redis_db'):
                ctx.redis_db = self.connect()
            return ctx.redis_db

    def increments(self, page) -> None:
        connection = self.connection
        connection.incr(page)

    def decrement(self, page) -> None:
        connection = self.connection
        connection.incr(page, -1)

    def get(self, page) -> int:
        connection = self.connection
        count = connection.get(page)
        return count if count else 0

counter = PageCounter()
