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
from flask_restful import Resource, abort

from App.api.api_utils import login_required
from App.models.models_constant import VIP_USER


class MovieOrdersResource(Resource):
    @login_required
    def post(self):
        user = g.user
        data = {
            "msg": "{}, post order ok".format(user.username)
        }

        return data


class MovieOrderResource(Resource):
    @login_required
    def put(self, order_id):

        user = g.user

        if not user.check_permission(VIP_USER):
            # 401, 身份验证是错的
            # 403，身份正确，但是权限不通过
            abort(403, msg="Permission denied.")

        data = {
            "msg": "order change success"
        }

        return data
