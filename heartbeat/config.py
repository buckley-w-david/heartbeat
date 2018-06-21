class HeartbeatConfig():
    DEBUG = False
    TESTING = False


class TestingConfig(HeartbeatConfig):
    TESTING = True


class DevelopmentConfig(HeartbeatConfig):
    DEBUG = True


class ProductionConfig(HeartbeatConfig):
    pass
