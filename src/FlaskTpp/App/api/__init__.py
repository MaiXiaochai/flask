# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : api_user.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/4 15:54
--------------------------------------
"""
from App.api.admin import api_admin
from App.api.cinema import api_cinema
from App.api.user import api_user


def init_api(app):
    api_admin.init_app(app)
    api_cinema.init_app(app)
    api_user.init_app(app)
