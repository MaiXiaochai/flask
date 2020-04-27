# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : third_blue.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 10:48
--------------------------------------
"""

from flask import Blueprint


third_blue = Blueprint("third_blue", __name__)


@third_blue.route("/third")
def hello_third():
    return "this is third blueprint!"
