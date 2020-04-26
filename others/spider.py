# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : spider.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/26 20:47
--------------------------------------
千锋教育Flask-2019下载地址
"""

from requests import get
from lxml import etree


def resp(url):
    response = get(url)
    return response


def selector(response):
    selector = etree.HTML(response.content)
    paths = selector.xpath("//li[@class='clearfix j-url-list']/a/@data-url")
    return paths


def main():
    url = "http://video.mobiletrain.org/course/index/courseId/672"
    res = resp(url)
    res = selector(res)

    for count, i in enumerate(res, 1):
        print(i)


if __name__ == "__main__":
    main()
