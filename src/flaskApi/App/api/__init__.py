# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : api.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/4 15:54
--------------------------------------
"""

from flask_restful import Api

from App.api.goods import GoodsResource, SingleGoodsResource
from App.api.hello import HelloResource

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(HelloResource, "/")
api.add_resource(GoodsResource, "/goods")
api.add_resource(SingleGoodsResource, "/goods/<int:id>", endpoint="single_goods")
