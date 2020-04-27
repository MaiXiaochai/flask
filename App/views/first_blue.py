# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : first_blue.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 9:11
--------------------------------------
"""

from flask import Blueprint

from App.models import models, User


first_blue = Blueprint("blue", __name__)


@first_blue.route("/<string:name>")
def hello(name):
    print(name)
    print(type(name))
    return "This is first blueprint, name: {}!".format(name)


@first_blue.route("/")
def hello_first():
    return "Hello Flask!"


@first_blue.route("/create_db")
def create_db():
    models.create_all()
    return "DB created."


@first_blue.route("/adduser")
def add_user():
    user = User()
    user.username = "Tom"

    models.session.add(user)
    models.session.commit()
    return "用户添加成功！"


@first_blue.errorhandler(404)
def error_404():
    return "404, 非常抱歉！"
