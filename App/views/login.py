# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : login.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/28 10:44
--------------------------------------
"""
from flask import Blueprint, request, render_template, Response, session

blue_login = Blueprint("login", __name__)


@blue_login.route("/login", methods=["GET", "POST"])
def login():
    method = request.method
    if method == "GET":
        return render_template("login.html")

    elif method == "POST":
        username = request.form.get("username")
        response = Response("{}，登录成功".format(username))
        # response.set_cookie("username", username)
        session['username'] = username
        return response


@blue_login.route("/cookie")
def get_cookie():
    username = session.get("username")
    result = "欢迎回来，{}!".format(username)
    return result
