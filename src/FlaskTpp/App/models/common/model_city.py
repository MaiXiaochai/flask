# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : model_city.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/12 18:35
--------------------------------------
"""
from App.ext import db
from App.models import BaseModel


class Letter(BaseModel):
    letter = db.Column(db.String(1), unique=True)


class City(BaseModel):
    letter_id = db.Column(db.Integer, db.ForeignKey(Letter.id))
    c_id = db.Column(db.Integer, default=0)
    parent_id = db.Column(db.Integer, default=0)
    region_name = db.Column(db.String(16))
    city_code = db.Column(db.Integer, default=0)
    pinyin = db.Column(db.String(64))
