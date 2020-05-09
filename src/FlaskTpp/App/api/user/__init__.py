# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : user.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/9 13:30
--------------------------------------
"""
from flask_restful import Api

from App.api.user.welcome import HelloResource

api_user = Api(prefix="/user")
api_user.add_resource(HelloResource, "/")
