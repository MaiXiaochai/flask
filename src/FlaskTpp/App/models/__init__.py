# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : models.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/26 22:20
--------------------------------------
"""


from App.ext import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        result = False
        try:
            db.session.add(self)
            db.session.commit()
            result = True
        except Exception as err:
            pass

        return result

    def delete(self):
        result = False
        try:
            db.session.delete(self)
            db.session.commit()
            result = True
        except Exception as err:
            pass

        return result
