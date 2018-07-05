#-*- coding: utf-8 -*-

from flask import Flask,redirect,url_for
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask_moment import Moment



app = Flask(__name__)
app.config.from_object(DevConfig)
bootstrap = Bootstrap(app)
moment = Moment(app)
##导入视图
views = __import__('views')



if __name__ == '__main__':
    app.run()
