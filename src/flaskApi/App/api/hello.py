# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : hello.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/4 16:42
--------------------------------------
"""

from flask_restful import Resource


class HelloResource(Resource):

    def get(self):
        return {"msg": "Hello, welcome to visit restful."}
