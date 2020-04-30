# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : blue_encrypt.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/30 16:07
--------------------------------------
"""
from time import time
from random import randrange
from os.path import dirname, abspath, join
from base64 import standard_b64encode, standard_b64decode

from flask import Blueprint, render_template, url_for, request

from App.models import models, News


blue_news = Blueprint("encrypt", __name__)


BASE_DIR = dirname(dirname(abspath(__file__)))


@blue_news.route("/addnews")
def add_news():
    news = News()
    news.n_title = "新闻-{}".format(randrange(100))
    content = ''
    counter = 0

    while counter < 20:
        content += str(randrange(48, 122))
        counter += 1
    news.n_content = content

    models.session.add(news)
    models.session.commit()

    return "[ News: {} | added.] [ Content: {} ]".format(news.n_title, news.n_content)


@blue_news.route("/news")
def get_news():
    news = News.query.all()
    news_content = render_template("news_content.html", news=news)

    key_1 = "hZ3xt5YTosPkvV8CmeTTg7o3Xo5eWVcj"
    key_2 = "6LQVWAWaG7gRAUEaWi5g3viqXEyHbBGK"
    # 加密过程： bytes -> base64 -> str -> key_1 + str + key_2
    content_encrypt = standard_b64encode(news_content.encode("utf-8")).decode("utf-8")
    content_salt = "{}{}{}".format(key_1, content_encrypt, key_2)

    return render_template("news.html", news_content=content_salt)


@blue_news.route("/getjs")
def get_js():
    time_arg = "2"
    try:
        time_arg = int(request.args.get("t"))
    except Exception as err:
        return time_arg

    time_current = time() * 1000
    diff = time_current - time_arg
    result = "1"

    if abs(diff) < 1000:
        with open(join(BASE_DIR, "static/js/show.js"), ) as f:
            result = f.read()

    return result
