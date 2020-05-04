"""
--------------------------------------
@File       : middleware.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/3 16:52
--------------------------------------
"""
from flask import request, current_app


def load_middleware(app):

    @app.before_request
    def before():
        pass

    @app.after_request
    def after(response):
        # current_app要在app.run()之后调用，之前调用请求不到
        config = current_app.config

        return response
