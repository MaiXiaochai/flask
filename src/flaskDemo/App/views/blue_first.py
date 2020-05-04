# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : blue_first.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 9:11
--------------------------------------
"""

from flask import Blueprint, render_template

from App.models import models, User


blue_first = Blueprint("blue", __name__)


@blue_first.route("/")
def hello_first():

    return "Hello Flask!"


@blue_first.route("/create_db")
def create_db():
    models.create_all()

    return "DB created."


@blue_first.route("/adduser")
def add_user():
    user = User()
    user.username = "Tom"

    models.session.add(user)
    models.session.commit()

    return "用户添加成功！"


@blue_first.route("/addusers")
def add_users():
    map_data = [dict(username="Tom-{}".format(i)) for i in range(10)]
    models.session.bulk_insert_mappings(User, map_data)
    models.session.commit()

    return "多个用户添加成功！"


@blue_first.route("/getuser")
def get_user():
    data = User.query.first()

    return "User: {}.".format(data.username)


@blue_first.route("/getuserbyid/<int:nbr>")
def get_user_by_id(nbr):
    data = User.query.get(nbr)

    return "User: {}.".format(data.username)


@blue_first.route("/filter")
def filter_data():
    # __gt__ 大于
    data = User.query.filter(User.id > 5)
    data = User.query.offset(1).limit(2)
    result = [i.username for i in data]
    return "Users: {}.".format(repr(result))


@blue_first.route("/filterby")
def filter_by():
    data = User.query.filter_by(id=20)
    result = ["{}: {}".format(i.id, i.username) for i in data]
    return "Users: {}.".format(repr(result))


@blue_first.route("/getusers")
def get_users():
    data = User.query.all()
    result = [i.username for i in data]

    return "All users: {}.".format(repr(result))


@blue_first.route("/delfirst")
def del_first():
    user = User.query.first()
    models.session.delete(user)
    models.session.commit()

    return "{}, deleted.".format(user.username)


@blue_first.route("/updtfirst")
def update_first():
    user = User.query.first()
    old_name = user.username
    user.username += "-UPDATED"
    models.session.add(user)
    models.session.commit()

    return "[{}] => [{}] [ UPDATED ].".format(old_name, user.username)


@blue_first.route("/paginate")
def paginate():
    users = User.query.paginate().items

    return render_template("users.html", users=users)


@blue_first.errorhandler(404)
def error_404():

    return "404, 非常抱歉！"
