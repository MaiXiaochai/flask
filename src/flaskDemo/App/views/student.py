# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : student.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/3 17:50
--------------------------------------
"""

from flask import Blueprint, request, render_template, flash, redirect, url_for

from App.ext import models
from App.models import Student
from App.utils import send_email

blue_student = Blueprint("student", __name__)


@blue_student.route("/register", methods=["GET", "POST"])
def register():
    method = request.method
    if method == "GET":
        return render_template("register.html")

    elif method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        student = Student.query.filter(Student.s_name == username).first()
        if student:
            flash("[{}, 已经被注册!]".format(student.s_name))

            return redirect(url_for("student.register"))

        student = Student()
        student.s_name = username
        student.s_password = password

        models.session.add(student)
        models.session.commit()

        return "[ Register succeed.]"


@blue_student.route("/login", methods=["GET", "POST"])
def login():
    method = request.method
    if method == "GET":
        return render_template("login.html")

    elif method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        student = Student.query.filter(Student.s_name == username).first()

        if student and student.check_password(password):

            return "[ Login succeed.]"

        else:
            flash("[用户名或密码不正确！]", "warning")

            return redirect(url_for("student.login"))


@blue_student.route("/sendemail")
def email():
    return send_email()
