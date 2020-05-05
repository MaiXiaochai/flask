# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : goods.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/4 18:26
--------------------------------------
"""
from flask import request
from flask_restful import Resource, abort, fields, marshal_with

from App.models import Goods

goods_fields = {
    "id": fields.Integer,
    "name": fields.String(attribute="g_name"),
    "g_price": fields.Float,
    # api.add_resource(SingleGoodsResource, "/goods/<int:id>", endpoint="single_goods")
    # 自己开发的时候可以加，上线之后别加
    "url": fields.Url("single_goods")
}

single_goods_fields = {
    "data": fields.Nested(goods_fields),
    "status": fields.Integer,
    "msg": fields.String(default="ok"),
    "others": fields.String
}

multi_goods_fields = {
    "status": fields.String,
    "msg": fields.String,
    "data": fields.List(fields.Nested(goods_fields))
}


class GoodsResource(Resource):
    """
    JSON格式
        Response
        1)单个对象
            {
                "status": 200,
                "msg": "ok",
                "data": {
                    "key1": "value1",
                    "key2": "value2",
                    "key3": "value3",
                    ...
                }
            }
        2)多个对象
            {
                "status": 200,
                "msg": "ok",
                "data": [
                    {
                        "key1": "value1",
                        "key2": "value2",
                        "key3": "value3",
                        ...
                    },
                    {
                        "key1": "value1",
                        "key2": "value2",
                        "key3": "value3",
                        ...
                    },
                    {
                        "key1": "value1",
                        "key2": "value2",
                        "key3": "value3",
                        ...
                    },
                    ...
                ]
            }
    """

    @marshal_with(multi_goods_fields)
    def get(self):
        goods = Goods.query.all()
        data = {
            "msg": "ok",
            "status": 200,
            "data": goods
        }
        return data

    @marshal_with(single_goods_fields)
    def post(self):
        g_name = request.form.get("g_name")
        g_price = request.form.get("g_price")

        goods = Goods()
        goods.g_name = g_name
        goods.g_price = g_price

        if not goods.save():
            abort(400)

        # 201 (Created/已创建)
        data = {
            "msg": "create success",
            "status": 201,
            # "data": marshal(goods, goods_fields)
            "data": goods
        }
        return data


class SingleGoodsResource(Resource):

    @marshal_with(single_goods_fields)
    def get(self, id):
        goods = Goods.query.get(id)

        data = {
            "status": 200,
            "msg": "ok",
            "data": goods
        }

        return data

    @marshal_with(single_goods_fields)
    def delete(self, id):
        goods = Goods.query.get(id)

        if not goods:
            abort(404)

        if not goods.delete():
            abort(400)

        data = {
            "msg": "Deleted",
            "status": 204
        }

        return data

    @marshal_with(single_goods_fields)
    def put(self, id):
        goods = Goods.query.get(id)

        if not goods:
            abort(404)

        g_name = request.form.get("g_name")
        g_price = request.form.get("g_price")

        goods.g_name = g_name
        goods.g_price = g_price

        if not goods.save():
            abort(400)

        data = {
            "msg": "Deleted",
            "status": 201,
            "data": goods
        }

        return data

    @marshal_with(single_goods_fields)
    def patch(self, id):
        goods = Goods.query.get(id)

        if not goods:
            abort(404)

        g_name = request.form.get("g_name")
        g_price = request.form.get("g_price")

        goods.g_name = g_name or goods.g_name
        goods.g_price = g_price or goods.g_price

        if not goods.save():
            abort(400)

        data = {
            "msg": "Deleted",
            "status": 201,
            "data": goods
        }

        return data
