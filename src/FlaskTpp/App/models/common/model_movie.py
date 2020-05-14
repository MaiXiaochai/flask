# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : model_movie.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/14 10:31
--------------------------------------
"""
from App.ext import db
from App.models import BaseModel


class Movies(BaseModel):
    __tablename__ = "movies"

    display_name = db.Column(db.String(64))
    performer = db.Column(db.String(128))
    director = db.Column(db.String(64))
    leading_role = db.Column(db.String(256))
    file_type = db.Column(db.String(64))
    country = db.Column(db.String(64))
    language = db.Column(db.String(64))
    duration = db.Column(db.Integer, default=90)
    screen_type = db.Column(db.String(32))
    release_date = db.Column(db.DateTime)
    bg_pic = db.Column(db.String(256))
    flag = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
