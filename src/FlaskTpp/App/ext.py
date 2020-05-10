# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : ext.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/4 15:59
--------------------------------------
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_caching import Cache

# SQLAlchemy 创建数据表，模型结构的修改，不会被映射到对应的数据表
# Migrate 作用是将models的结构修改映射到数据库中
db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={
    "CACHE_TYPE": "simple"
})


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    Session(app)
    cache.init_app(app)
