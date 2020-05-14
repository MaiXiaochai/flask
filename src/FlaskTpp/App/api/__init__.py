# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : api_movie_user.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/4 15:54
--------------------------------------
"""
from .admin import api_admin
from .cinema import api_cinema
from .user import api_user
from .common import api_common


def init_api(app):
    api_admin.init_app(app)
    api_cinema.init_app(app)
    api_user.init_app(app)
    api_common.init_app(app)
