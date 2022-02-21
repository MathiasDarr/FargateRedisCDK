class BaseConfig(object):
    APP_NAME ="Nardis API"
    AWS_REGION = "us-west-2"
    NARDIS_S3_BUCKET = "nardis-bucket"
    FLASK_RUN_PORT = 8080
    FLASK_RUN_HOST = "127.0.0.1"
    VALUE = "v1"

    @staticmethod
    def configure(app):
        from os import environ
        environ["FLASK_ENV"] = app.config["FLASK_ENV"]


class TestingConfig(BaseConfig):
    DEBUG = True
    FLASK_ENV = "development"
    VALUE = "testing_value"


class DevConfig(BaseConfig):
    DEBUG = True
    FLASK_ENV = "development"
    VALUE = "dev_value"

class ProdConfig(BaseConfig):
    DEBUG = False
    FLASK_ENV = "development"
    VALUE = "prod_value"

config = dict(
    dev=DevConfig,
    prod=ProdConfig,
    testing=TestingConfig
)