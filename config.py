from webapp import app
import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'asd32f243'
    DB_NAME = 'prod-db'
    # CSRF_ENABLED = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = 'dev-db'
    path = f"sqlite:///{os.path.abspath('test1.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = path
