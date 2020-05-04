# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : manager.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/26 22:05
--------------------------------------
"""
from os import environ

from flask_script import Manager
from flask_migrate import MigrateCommand

from App import create_app

env = environ.get("FLASK_ENV", "default")
app = create_app(env)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()
