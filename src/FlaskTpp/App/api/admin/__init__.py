# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : admin.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/9 13:29
--------------------------------------
"""
from flask_restful import Api

from App.api.admin.api_admin_user import AdminUserResource

api_admin = Api(prefix="/admin")
api_admin.add_resource(AdminUserResource, "/users")
