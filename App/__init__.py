# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : __init__.py.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/26 22:05
--------------------------------------
"""
from flask import Flask

from App.views import blue


def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blue)
    return app
