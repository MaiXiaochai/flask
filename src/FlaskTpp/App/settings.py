# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : settings.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 14:03
--------------------------------------
"""

from App.ext import db


def get_db_uri(db_info):
    """
    "oracle+cx_oracle://sched:sched123@192.168.158.219:1521/?service_name=bfcecdw"
    :param db_info:     dict
    :return:            str
    """
    uri_tpl = "{engine}+{driver}://{user}:{password}@{host}:{port}/{name}"
    uri = uri_tpl.format(**db_info)

    return uri


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "4)rzG[giX:{>)2>_Np'`X-Q&YZFzj@5-"
    SESSION_USE_SIGNER = True  # 对发送到浏览器上的cookie进行加密
    SESSION_TYPE = "sqlalchemy"
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SESSION_SQLALCHEMY = db

    # # 缓存设置
    # 缓存类型
    CACHE_TYPE = "filesystem"
    # 缓存类型为"filesystem"时，该值要指定。
    # 注意：指定的是目录，不是文件
    CACHE_DIR = "cache"
    # 缓存数据超时时间(seconds)
    CACHE_DEFAULT_TIMEOUT = 60 * 60 * 24 * 30

    # # 邮箱配置
    MAIL_SERVER = "smtp.163.com"
    # 163 SSL协议端口 465/994, 非SSL协议端口25
    # 注意这里启用的是TLS协议(transport layer security)，而不是SSL协议所用的是25号端口
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = "chargestarmap@163.com"
    # 163这里用的是授权码
    MAIL_PASSWORD = """RYLVFPIMSJSDKVTD"""
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevelopConfig(Config):
    DEBUG = True
    db_info = {
        "engine": "mysql",
        "driver": "pymysql",
        "user": "sched",
        "password": "sched123",
        "host": "127.0.0.1",
        "port": 1521,
        "name": "Snail"
    }
    # ORM 数据库连接串
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite.db"


class TestingConfig(Config):
    TESTING = True
    db_info = {
        "engine": "mysql",
        "driver": "pymysql",
        "user": "sched",
        "password": "sched123",
        "host": "127.0.0.1",
        "port": 1521,
        "name": "Snail"
    }
    # ORM 数据库连接串
    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


class StagingConfig(Config):
    db_info = {
        "engine": "mysql",
        "driver": "pymysql",
        "user": "sched",
        "password": "sched123",
        "host": "127.0.0.1",
        "port": 1521,
        "name": "Snail"
    }
    # ORM 数据库连接串
    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


class ProductConfig(Config):
    db_info = {
        "engine": "mysql",
        "driver": "pymysql",
        "user": "sched",
        "password": "sched123",
        "host": "127.0.0.1",
        "port": 1521,
        "name": "Snail"
    }
    # ORM 数据库连接串
    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


envs = {
    "development": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductConfig,
    "default": DevelopConfig,
}
