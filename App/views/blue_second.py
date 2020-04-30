# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : blue_second.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/4/27 9:14
--------------------------------------
"""
from random import randrange

from flask import Blueprint, request, render_template
from sqlalchemy import and_, or_

from App.ext import cache
from App.models import models, Customer, Address

blue_second = Blueprint("blue_second", __name__)


@blue_second.route("/second")
def hello_second(address):

    return "This is second blueprint, path: {}!".format(address)


@blue_second.route("/addcustomer")
def add_customer():
    customer = Customer()
    res = customer.c_name = "Jerry{}".format(randrange(1000))

    models.session.add(customer)
    models.session.commit()

    return "[ {} ][ 用户添加成功 ]".format(res)


@blue_second.route("/addaddr")
def add_address():
    address = Address()
    res = address.a_position = "半人马座-{}".format(randrange(1000))
    # 注意这里倒序的写法
    address.a_customer_id = Customer.query.order_by(Customer.id.desc()).first().id

    models.session.add(address)
    models.session.commit()

    return "[ {} ][ 地址添加成功 ]".format(res)


@blue_second.route("/addrbyid")
def get_addr_by_id():
    c_id = request.args.get("id")
    customer = Customer.query.get(c_id)
    # addrs = Address.query.filter_by(a_customer_id=customer.id)
    addrs = customer.address

    return render_template("addrlist.html", addrs=addrs)


@blue_second.route("/search")
@cache.cached(timeout=60)
def search():
    # addrs = Address.query.filter(Address.a_customer_id == 9).filter(Address.a_position.endswith("4"))
    addrs = Address.query.filter(
        or_(
            Address.a_customer_id == 9,
            Address.a_position.endswith("4")
        )
    )
    print("[ 从数据库查询。]")
    return render_template("addrlist.html", addrs=addrs)
