# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : __init__.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/26 22:20
--------------------------------------
"""

from .first_blue import first_blue
from .second_blue import second_blue
from .third_blue import third_blue


def init_views(app):
    app.register_blueprint(first_blue)
    app.register_blueprint(second_blue)
    app.register_blueprint(third_blue)
