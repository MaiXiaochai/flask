# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : api_movie_user.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/9 14:51
--------------------------------------
"""
import uuid

from flask_restful import Resource, abort, fields, marshal
from flask_restful.reqparse import RequestParser

from App.api.api_constant import *
from App.ext import cache
from App.models.model_utils import get_user
from App.models.user import User

parser_base = RequestParser()
parser_base.add_argument("password", type=str, required=True, help="请输入密码")
parser_base.add_argument("action", type=str, required=True, help="请输入要进行的事项")

# 注册用args
parser_register = parser_base.copy()
parser_register.add_argument("username", type=str, required=True, help="请输入用户名")
parser_register.add_argument("phone", type=str, required=True, help="请输入手机号")

# 登录用args, 区别在于username和phone字段中去掉了required=True
parser_login = parser_base.copy()
parser_login.add_argument("username", type=str, help="请输入用户名")
parser_login.add_argument("phone", type=str, help="请输入手机号")

# Response 中使用的模板
base_user_fields = {
    "username": fields.String,
    "phone": fields.String
}

user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(base_user_fields)
}


class MovieUserResource(Resource):
    def post(self):
        """
        用户注册和登录
        """
        args = parser_base.parse_args()

        action = args.get("action", "-").lower()
        password = args.get("password")

        # 用户注册
        if action == USER_ACTION_REGISTER:
            args_register = parser_register.parse_args()

            user = User()
            user.username = args_register.get("username")
            user.password = password
            user.phone = args_register.get("phone")

            if not user.save():
                abort(400, msg="用户注册失败.")

            data = {
                "status": HTTP_CREATE_OK,
                "msg": "用户创建成功",
                "data": user
            }
            return marshal(data, user_fields)

        # 用户登录
        elif action == USER_ACTION_LOGIN:
            args_login = parser_login.parse_args()
            username = args_login.get("username")
            phone = args_login.get("phone")

            user = get_user(username) or get_user(phone)

            if not user:
                abort(400, msg="用户不存在")

            if not user.check_password(password):
                abort(401, msg="密码错误")

            if user.is_deleted:
                abort(401, msg="用户已标记为注销")

            token = uuid.uuid4().hex
            cache.set(token, user.id)

            data = {
                "msg": "login success",
                "status": HTTP_OK,
                "token": token
            }

            return data

        else:
            abort(400, msg="请提供正确的参数!")
