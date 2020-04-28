# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : blue_second.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 9:14
--------------------------------------
"""

from flask import Blueprint


blue_second = Blueprint("blue_second", __name__)


@blue_second.route("/second")
def hello_second(address):
    return "This is second blueprint, path: {}!".format(address)

