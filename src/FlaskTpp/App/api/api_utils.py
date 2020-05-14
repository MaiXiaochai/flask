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

from App.api.api_constant import USER_TYPE_MOVIE, USER_TYPE_ADMIN
from App.ext import cache
from App.models.model_utils import get_movie_user, get_admin_user
from App.models.model_constant import MSG_403


def _verify(user_type):
    """
    验证不同类型的 token
    :param user_type:   用户类型
    """

    def _get_user(_type):
        func = None
        if _type == USER_TYPE_MOVIE:
            func = get_movie_user

        elif _type == USER_TYPE_ADMIN:
            func = get_admin_user
            print("USER_TYPE_ADMIN")
        return func

    def check_token(_token, _type):
        if not _token:
            abort(401, msg="not login")

        elif not _token.startswith(_type):
            abort(403, msg="Permission denied.")

    token = request.args.get("token")
    check_token(token, user_type)

    user_id = cache.get(token)
    if not user_id:
        abort(401, msg="user not available")

    user = _get_user(user_type)(user_id)

    if not user:
        abort(401, msg="user not available")

    # 用全局的g传递数据
    g.user = user
    g.token = token


def required_login(user_type):
    """
    登录验证，装饰器
    """

    def inner(func):
        def wrapper(*args, **kwargs):
            _verify(user_type)

            return func(*args, **kwargs)

        return wrapper

    return inner


def required_permission(permission):
    """
    登录和权限验证，装饰器
    TODO: 改成可以判断 movie_user 和 admin_user
    """

    def require_permission_wrapper(func):
        def wrapper(*args, **kwargs):
            _verify(USER_TYPE_MOVIE)

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
