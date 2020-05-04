# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : models.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/26 22:20
--------------------------------------
"""
from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import models


class User(models.Model):
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    username = models.Column(models.String(16))


class Customer(models.Model):
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    c_name = models.Column(models.String(30))
    address = models.relationship("Address", backref="customer", lazy=True)


class Address(models.Model):
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    a_position = models.Column(models.String(128))
    # 这里的外键中，传入的值为字符串也可以，"Customer.id"
    a_customer_id = models.Column(models.Integer, models.ForeignKey(Customer.id))


class News(models.Model):
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    n_title = models.Column(models.String(32))
    n_content = models.Column(models.String(256))


class Student(models.Model):
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    s_name = models.Column(models.String(16), unique=True)
    _s_password = models.Column(models.String(256))
    _s_phone = models.Column(models.String(32), unique=True)

    @property
    def s_password(self):
        raise Exception("Error Action: You have no access to password.")

    @s_password.setter
    def s_password(self, password):
        self._s_password = generate_password_hash(password)

    def check_password(self, password):

        return check_password_hash(self._s_password, password)
