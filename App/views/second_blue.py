# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : second_blue.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 9:14
--------------------------------------
"""

from flask import Blueprint


second_blue = Blueprint("second_blue", __name__)


@second_blue.route("/second")
def hello_second(address):
    return "This is second blueprint, path: {}!".format(address)

