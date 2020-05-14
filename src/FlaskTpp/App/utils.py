# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : utils.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/14 18:09
--------------------------------------
"""
from uuid import uuid4

from App.api.api_constant import USER_TYPE_MOVIE, USER_TYPE_ADMIN, USER_TYPE_CINEMA
from App.settings import UPLOAD_DIR, FILE_PATH


def gen_token(prefix=None):
    """
    :param prefix:      str     前缀
    :return:            str     token值
    """
    token = prefix + uuid4().hex
    return token


def gen_token_movie_user():
    return gen_token(USER_TYPE_MOVIE)


def gen_token_admin_user():
    return gen_token(USER_TYPE_ADMIN)


def gen_token_cinema_user():
    return gen_token(USER_TYPE_CINEMA)


def filename_transfer(filename):
    """
    转换文件名称
    :param filename:        str                 原始文件名称
    :return:                tuple/(str, str)    (绝对路径， 相对路径)
    """
    suffix = filename.rsplit(".", 1)[-1]
    new_name = "{}.{}".format(uuid4().hex, suffix)
    abs_path = "{}/{}".format(UPLOAD_DIR, new_name)
    rel_path = "{}/{}".format(FILE_PATH, new_name)

    return abs_path, rel_path
