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
