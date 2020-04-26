# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : views.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/26 22:20
--------------------------------------
"""
from flask import Blueprint


blue = Blueprint("blue", __name__)


@blue.route("/")
def hello():
    return "Hello Flask!"


@blue.route("/blue")
def hello_blue():
    return "BluePrint!"
