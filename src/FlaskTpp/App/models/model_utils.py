# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : model_utils.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/10 18:00
--------------------------------------
"""
from App.models.admin import AdminUser
from App.models.user import MovieUser


def get_movie_user(user_ident):
    """
    获取客户端用户
    """
    found = False

    if not user_ident:
        return found

    query_obj = MovieUser.query

    # 根据 id
    by_id = query_obj.get(user_ident)

    if by_id:
        found = by_id

    elif not found:
        by_name = query_obj.filter(MovieUser.username == user_ident).first()
        if by_name:
            found = by_name

    else:
        by_phone = query_obj.filter(MovieUser.phone == user_ident).first()
        if by_phone:
            found = by_phone

    return found


def get_admin_user(user_ident):
    found = False

    if not user_ident:
        return found

    query_obj = AdminUser.query

    # 根据 id
    by_id = query_obj.get(user_ident)

    if by_id:
        found = by_id

    elif not found:
        by_name = query_obj.filter(AdminUser.username == user_ident).first()
        if by_name:
            found = by_name

    return found
