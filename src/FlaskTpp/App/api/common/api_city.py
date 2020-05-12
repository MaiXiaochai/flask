# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : api_city.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/12 19:07
--------------------------------------
"""
from flask_restful import Resource


class CitiesResource(Resource):
    def get(self):

        data = {
            "msg": "城市列表"
        }
        return data
