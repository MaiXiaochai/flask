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
from App.models.model_constant import USER_VIP


class MovieOrdersResource(Resource):
    @required_login
    def post(self):
        """
        获取订单
        http://127.0.0.1:5000/users/orders?token=764ae3383e6a4267ac58cfab741bf495
        """
        data = {
            "msg": "订单获取成功."
        }

        return data


class MovieOrderResource(Resource):
    @required_permission(USER_VIP)
    def put(self, order_id):
        """
        修改订单
        http://127.0.0.1:5000/users/orders/1?token=764ae3383e6a4267ac58cfab741bf495
        """
        data = {
            "msg": "订单修改成功."
        }

        return data
