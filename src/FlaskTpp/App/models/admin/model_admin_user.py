# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : model_admin_user.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/13 22:44
--------------------------------------
"""
from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models import BaseModel
from App.models.model_constant import ADMIN_COMMON


class AdminUser(BaseModel):
    username = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    is_deleted = db.Column(db.Boolean, default=False)
    is_supper = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=ADMIN_COMMON)

    @property
    def password(self):
        raise Exception("You have no access to password.")

    @password.setter
    def password(self, passwd):
        self._password = generate_password_hash(passwd)

    def check_password(self, passwd):
        return check_password_hash(self._password, passwd)

    def check_permission(self, permission):
        # 权限值与运算判断权限，
        # 与之后，相同，则有权限，不同则无权限
        return self.is_supper or permission & self.permission == permission
