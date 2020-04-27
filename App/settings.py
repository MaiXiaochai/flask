# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : settings.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 14:03
--------------------------------------
"""
from os.path import dirname, abspath

BASE_DIR = dirname(dirname(abspath(__file__)))


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
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRECT_KEY = "aoQx2op3!EeJ1d^p77aGduDo7K&f%bqm"


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
