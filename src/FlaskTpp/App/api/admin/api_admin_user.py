# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : api_admin_user.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/13 23:03
--------------------------------------
"""

import uuid

from flask_restful import Resource, abort, fields, marshal
from flask_restful.reqparse import RequestParser

from App.api.api_constant import *
from App.ext import cache
from App.models.model_utils import get_admin_user
from App.models.admin import AdminUser

parser_admin = RequestParser()
parser_admin.add_argument("password", type=str, required=True, help="请输入密码")
parser_admin.add_argument("action", type=str, required=True, help="请输入要进行的事项")
parser_admin.add_argument("username", type=str, required=True, help="请输入用户名")

# Response 中使用的模板
base_admin_fields = {
    "username": fields.String
}

admin_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(base_admin_fields)
}


class AdminUserResource(Resource):
    def post(self):
        """
        用户注册和登录
        注册：
            http://127.0.0.1:5000/admin/users?action=register
            {
                "username": "admin",
                "password": "123"
            }
        登录：
            http://127.0.0.1:5000/admin/users?action=login
            {
                "username": "admin",
                "password": "123"
            }
            Response:
                {
                    "msg": "login success",
                    "status": 200,
                    "token": "8c68005c93f048dbbfbe73770a2add53"
                }
        """
        args = parser_admin.parse_args()

        action = args.get("action", "-").lower()
        password = args.get("password")

        # 用户注册
        if action == USER_ACTION_REGISTER:
            args_register = parser_admin.parse_args()

            admin_user = AdminUser()
            admin_user.username = args_register.get("username")
            admin_user.password = password

            if not admin_user.save():
                abort(400, msg="用户注册失败.")

            data = {
                "status": HTTP_CREATE_OK,
                "msg": "用户创建成功",
                "data": admin_user
            }
            return marshal(data, admin_fields)

        # 用户登录
        elif action == USER_ACTION_LOGIN:
            args_login = parser_admin.parse_args()
            username = args_login.get("username")

            admin_user = get_admin_user(username)

            if not admin_user:
                abort(400, msg="用户不存在")

            if not admin_user.check_password(password):
                abort(401, msg="密码错误")

            if admin_user.is_deleted:
                abort(401, msg="用户已标记为注销")

            token = uuid.uuid4().hex
            cache.set(token, admin_user.id)

            data = {
                "msg": "login success",
                "status": HTTP_OK,
                "token": token
            }

            return data

        else:
            abort(400, msg="请提供正确的参数!")
