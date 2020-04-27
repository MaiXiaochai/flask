# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : ext.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 14:03
--------------------------------------
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# SQLAlchemy 创建数据表，模型结构的修改，不会被映射到对应的数据表
# Migrate 作用是将models的结构修改映射到数据库中
models = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    models.init_app(app)
    migrate.init_app(app, models)
