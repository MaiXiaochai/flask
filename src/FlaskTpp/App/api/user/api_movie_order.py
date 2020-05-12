# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : api_movie_order.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/10 19:21
--------------------------------------
"""
from flask import g
from flask_restful import Resource

from App.api.api_utils import required_login, required_permission
from App.models.models_constant import USER_VIP


class MovieOrdersResource(Resource):
    @required_login
    def post(self):
        user = g.user
        data = {
            "msg": "订单获取成功."
        }

        return data


class MovieOrderResource(Resource):
    @required_permission(USER_VIP)
    def put(self, order_id):
        data = {
            "msg": "order change success"
        }

        return data
