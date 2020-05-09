# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : __init__.py.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/4 15:54
--------------------------------------
"""

from flask import Flask

from App.api import init_api
from App.settings import envs
from App.ext import init_ext


def create_app(env):
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(envs.get(env))

    # 初始化扩展
    init_ext(app)

    # 初始化API
    init_api(app)

    return app
