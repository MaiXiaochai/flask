# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : models.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/26 22:20
--------------------------------------
"""
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
