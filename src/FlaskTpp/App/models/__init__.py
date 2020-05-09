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


class BaseModel(models.Model):
    __abstract__ = True
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)

    def save(self):
        result = False
        try:
            models.session.add(self)
            models.session.commit()
            result = True
        except Exception as err:
            pass

        return result

    def delete(self):
        result = False
        try:
            models.session.delete(self)
            models.session.commit()
            result = True
        except Exception as err:
            pass

        return result
