# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : api_movie_user.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/9 13:30
--------------------------------------
"""
from flask_restful import Api

from App.api.user.api_movie_user import MovieUserResource
from App.api.user.api_movie_order import MovieOrderResource

api_user = Api(prefix="/users")

api_user.add_resource(MovieUserResource, "/")
api_user.add_resource(MovieOrderResource, "/orders")
