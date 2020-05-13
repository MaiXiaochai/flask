# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : api_utils.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/11 1:32
--------------------------------------
"""

from flask import request, g
from flask_restful import abort

from App.ext import cache
from App.models.model_utils import get_movie_user
from App.models.model_constant import MSG_403


def _verify():
    token = request.args.get("token")
    if not token:
        abort(401, msg="not login")

    user_id = cache.get(token)
    if not user_id:
        abort(401, msg="user not available")

    user = get_movie_user(user_id)
    if not user:
        abort(401, msg="user not available")

    # 用全局的g传递数据
    g.user = user
    g.token = token


def required_login(func):
    """
    登录验证，装饰器
    """

    def wrapper(*args, **kwargs):
        _verify()

        return func(*args, **kwargs)

    return wrapper


def required_permission(permission):
    """
    登录和权限验证，装饰器
    """

    def require_permission_wrapper(func):
        def wrapper(*args, **kwargs):
            _verify()

            if not g.user.check_permission(permission):
                abort(403, msg=MSG_403)

            return func(*args, **kwargs)

        return wrapper

    return require_permission_wrapper


def file_data(file_path):
    """
    读取文件中的数据
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
        return data
