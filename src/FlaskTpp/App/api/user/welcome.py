# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : welcome.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/9 14:51
--------------------------------------
"""
from flask_restful import Resource


class HelloResource(Resource):
    def get(self):
        result = {
            "msg": "Welcome to Taopiaopiao!"
        }
        return result
