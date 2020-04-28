# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : __init__.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/26 22:20
--------------------------------------
"""

from .blue_first import blue_first
from .blue_second import blue_second
from .blue_third import blue_third
from .login import blue_login


def init_views(app):
    app.register_blueprint(blue_first)
    app.register_blueprint(blue_second)
    app.register_blueprint(blue_third)
    app.register_blueprint(blue_login)
