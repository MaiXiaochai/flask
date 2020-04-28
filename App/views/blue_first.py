# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : blue_first.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 9:11
--------------------------------------
"""

from flask import Blueprint

from App.models import models, User


blue_first = Blueprint("blue", __name__)


@blue_first.route("/")
def hello_first():
    return "Hello Flask!"


@blue_first.route("/create_db")
def create_db():
    models.create_all()
    return "DB created."


@blue_first.route("/adduser")
def add_user():
    user = User()
    user.username = "Tom"

    models.session.add(user)
    models.session.commit()
    return "用户添加成功！"


@blue_first.route("/addusers")
def add_users():
    map_data = [dict(username="Tom-{}".format(i)) for i in range(10)]
    models.session.bulk_insert_mappings(User, map_data)
    models.session.commit()
    return "多个用户添加成功！"


@blue_first.errorhandler(404)
def error_404():
    return "404, 非常抱歉！"
