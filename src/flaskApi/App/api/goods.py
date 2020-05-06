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
from flask_restful.reqparse import RequestParser
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
    "msg": fields.String(default="ok")
}

multi_goods_fields = {
    "status": fields.String,
    "msg": fields.String,
    "data": fields.List(fields.Nested(goods_fields))
}

parser = RequestParser()
parser.add_argument("g_name", type=str, required=True, help="缺少g_name或者g_name值为空")
parser.add_argument("g_price")


class GoodsResource(Resource):

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
        # g_name = request.form.get("g_name")
        # g_price = request.form.get("g_price")
        args = parser.parse_args()
        g_name = args.get("g_name")
        g_price = args.get("g_price")

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
            # abort(http_status_code, **kwargs)
            # kwargs 的内容会被添加到返回的信息中
            abort(404, message="goods doesn't exist.", msg="fail")

        if not goods.delete():
            abort(400)

        data = {
            "msg": "Deleted",
            "status": 204,
            "data": goods
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
