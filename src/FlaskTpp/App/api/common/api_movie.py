# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : api_movie.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/14 11:08
--------------------------------------
"""

from flask_restful import Resource, abort, marshal, fields
from flask_restful.reqparse import RequestParser
from werkzeug.datastructures import FileStorage

from App.api.api_constant import USER_TYPE_ADMIN, HTTP_CREATE_OK
from App.api.api_utils import required_login
from App.models.common import Movies
from App.utils import filename_transfer, str_to_date

parser = RequestParser()

parser.add_argument("display_name", required=True, help="no display_name")
parser.add_argument("performer", required=True, help="no performer")
parser.add_argument("director", required=True, help="no director")
parser.add_argument("leading_role", required=True, help="no leading_role")
parser.add_argument("file_type", required=True, help="no file_type")
parser.add_argument("country", required=True, help="no country")
parser.add_argument("language", required=True, help="no language")
parser.add_argument("duration", required=True, help="no duration")
parser.add_argument("screen_type", required=True, help="no screen_type")
parser.add_argument("release_date", required=True, help="no release_date")
parser.add_argument("bg_pic", type=FileStorage, required=True, help="no bg_pic", location=["files"])

movie_fields = {
    "display_name": fields.String,
    "performer": fields.String,
    "director": fields.String,
    "leading_role": fields.String,
    "file_type": fields.String,
    "country": fields.String,
    "language": fields.String,
    "duration": fields.Integer,
    "screen_type": fields.String,
    "release_date": fields.String,
    "bg_pic": fields.String
}


class MoviesResource(Resource):
    """
    超级管理员:
    snail/123
    admin_userd6cff5606bda4ebfa31554b76be1f296
    """

    def get(self):
        result = {
            "msg": "获取电影列表成功"
        }
        return result

    @required_login(USER_TYPE_ADMIN)
    def post(self):
        args = parser.parse_args()
        movie = Movies()

        movie.display_name = args.get("display_name")
        movie.performer = args.get("performer")
        movie.director = args.get("director")
        movie.leading_role = args.get("leading_role")
        movie.file_type = args.get("file_type")
        movie.country = args.get("country")
        movie.language = args.get("language")
        movie.duration = args.get("duration")
        movie.screen_type = args.get("screen_type")
        movie.release_date = str_to_date(args.get("release_date"))

        file_content = args.get("bg_pic")
        # 安全处理、转换文件名称
        abs_path, rel_path = filename_transfer(file_content.filename)

        # 保存
        file_content.save(abs_path)
        movie.bg_pic = rel_path

        if not movie.save():
            abort(400, msg="电影信息添加失败")

        result = {
            "msg": "电影信息添加成功",
            "status": HTTP_CREATE_OK,
            "data": marshal(movie, movie_fields)
        }

        return result
