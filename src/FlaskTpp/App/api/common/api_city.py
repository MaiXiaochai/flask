# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : api_city.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/12 19:07
--------------------------------------
"""
from json import loads

from flask_restful import Resource, abort, fields, marshal
from flask_restful.reqparse import RequestParser

from App.api.api_constant import USER_ACTION_ADD_CITY, HTTP_OK, USER_TYPE_MOVIE
from App.api.api_utils import required_login, file_data
from App.models.common import City, Letter

parser_city = RequestParser()
parser_city.add_argument("action", type=str, help="请输入动作")

city_fields = {
    "id": fields.Integer(attribute="c_id"),
    "parentId": fields.Integer(attribute="parent_id"),
    "regionName": fields.String(attribute="region_name"),
    "cityCode": fields.String(attribute="city_code"),
    "pinYin": fields.String(attribute="pinyin")
}


class CitiesResource(Resource):
    """
    插入城市数据到数据库中
    http://127.0.0.1:5000/common/cities?action=add_city&token=movie_userebe6401abc564df487d6295743c30f40
    """

    def get(self):
        result = {}
        cities_fields = {}
        letters = Letter.query.all()

        for letter in letters:
            cities = City.query.filter_by(letter_id=letter.id)
            result[letter.letter] = cities

            cities_fields[letter.letter] = fields.List(fields.Nested(city_fields))

        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": marshal(result, cities_fields)
        }
        return data

    @required_login(USER_TYPE_MOVIE)
    def post(self):
        action = parser_city.parse_args().get("action")
        file_path = "App/data/cities.json"

        if action and action.lower() == USER_ACTION_ADD_CITY:
            len_letter = len(Letter().query.all())
            len_city = len(City().query.all())

            if len_letter > 1:
                result = {
                    "msg": "城市数据已存在.",
                    "status": HTTP_OK,
                    "total": {
                        "letters": len_letter,
                        "cities": len_city
                    }
                }

                return result

            else:
                count_letter, count_city = 0, 0
                data = loads(file_data(file_path)).get("returnValue")

                for _letter in data:
                    letter = Letter()

                    letter.letter = _letter
                    letter.save()
                    count_letter += 1

                    for _city in data.get(_letter):
                        city = City()

                        letter_id = Letter.query.filter(Letter.letter == _letter).first().id

                        city.letter_id = letter_id
                        city.c_id = _city.get("id")
                        city.parent_id = _city.get("parentId")
                        city.region_name = _city.get("regionName")
                        city.city_code = _city.get("cityCode")
                        city.pinyin = _city.get("pinYin")

                        city.save()
                        count_city += 1

                result = {
                    "msg": "城市数据插入成功.",
                    "status": HTTP_OK,
                    "total": {
                        "letters": count_letter,
                        "cities": count_city
                    }
                }

                return result

        else:
            abort(403, msg="无法识别 action.")
