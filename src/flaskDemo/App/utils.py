# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : utils.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/4 8:08
--------------------------------------
"""
from flask_mail import Message

from App.ext import mail


def send_email():
    msg = Message(
        "Flask email",
        recipients=["chargestarmap@163.com"],
                  )
    msg.body = "The first email from Flask."
    msg.html = "<h>Hello Flask-Email</h>"

    mail.send(msg)

    return "[ Email sent.]"
