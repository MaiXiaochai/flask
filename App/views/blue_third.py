# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : blue_third.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 10:48
--------------------------------------
"""

from flask import Blueprint


blue_third = Blueprint("blue_third", __name__)


@blue_third.route("/third")
def hello_third():
    return "this is third blueprint!"
