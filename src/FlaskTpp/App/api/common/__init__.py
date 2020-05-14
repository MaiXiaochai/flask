# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : __init__.py.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/12 19:04
--------------------------------------
"""

from flask_restful import Api

from .api_city import CitiesResource
from .api_movie import MoviesResource

api_common = Api(prefix="/common")
api_common.add_resource(CitiesResource, "/cities")
api_common.add_resource(MoviesResource, "/movies")
