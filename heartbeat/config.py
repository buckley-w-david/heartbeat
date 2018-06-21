import os


class HeartbeatConfig:
    DEBUG = False
    TESTING = False
    REDIS_HOST = 'localhost'
    REDIS_PORT = '6379'
    REDIS_DB = '0'


class TestingConfig(HeartbeatConfig):
    TESTING = True


class DevelopmentConfig(HeartbeatConfig):
    DEBUG = True


class ProductionConfig(HeartbeatConfig):
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
    REDIS_DB = os.environ.get('REDIS_DB', '0')
