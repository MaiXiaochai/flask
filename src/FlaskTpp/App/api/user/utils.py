# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : utils.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/11 1:32
--------------------------------------
"""
from flask import request, g
from flask_restful import abort

from App.ext import cache
from App.models.model_utils import get_user


def login_required(func):
    def wrapper(*args, **kwargs):
        token = request.args.get("token")
        if not token:
            abort(401, msg="not login")

        user_id = cache.get(token)
        if not user_id:
            abort(401, msg="user not available")

        user = get_user(user_id)
        if not user:
            abort(401, msg="user not available")
        
        # 用全局的g传递数据
        g.user = user
        g.token = token

        return func(*args, **kwargs)
    return wrapper
