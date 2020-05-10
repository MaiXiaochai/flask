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

from App.api.user.utils import login_required


class MovieOrderResource(Resource):
    @login_required
    def post(self):

        user = g.user
        print(user.username)
        data = {
            "msg": "post order ok"
        }

        return data
