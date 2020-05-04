# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : __init__.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/26 22:05
--------------------------------------
"""
from flask import Flask

from App.settings import envs
from App.ext import init_ext
from App.views import init_views
from App.middleware import load_middleware


def create_app(env):
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(envs.get(env))

    # 初始化扩展
    init_ext(app)

    # 初始化路由
    init_views(app)

    # 加载中间件
    load_middleware(app)

    return app
