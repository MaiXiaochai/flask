# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : app.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 15:56
--------------------------------------
"""
from os import environ

from App import create_app

env = environ.get("FLASK_ENV", "default")
app = create_app(env)


if __name__ == "__main__":
    app.run()
