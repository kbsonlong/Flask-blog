#-*- coding: utf-8 -*-

from flask import Flask,redirect,url_for
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask_moment import Moment



app = Flask(__name__)
app.config.from_object(DevConfig)
bootstrap = Bootstrap(app)
moment = Moment(app)
views = __import__('views')


# @app.route('/')
# def home():
#     return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()
