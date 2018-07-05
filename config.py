import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Base config class."""
    SECRET_KEY = '1a8fe304639d48fc1276735fdc39a8aa'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProdConfig(Config):
    """Production config class"""
    pass

class DevConfig(Config):
    """Development config class"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:kbsonlong@blog_db:8080/blog'
