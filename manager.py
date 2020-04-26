# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : manager.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/26 22:05
--------------------------------------
"""

from flask_script import Manager

from App import create_app

app = create_app()
manager = Manager(app)


if __name__ == "__main__":
    manager.run()
