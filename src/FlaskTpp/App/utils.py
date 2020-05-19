# -*- coding: utf-8 -*-

"""
--------------------------------------
@File       : utils.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@Created on : 2020/5/14 18:09
--------------------------------------
"""
from datetime import datetime
from random import sample
from uuid import uuid4

from openpyxl import Workbook
from werkzeug.utils import secure_filename

from App.api.api_constant import USER_TYPE_MOVIE, USER_TYPE_ADMIN, USER_TYPE_CINEMA
from App.settings import UPLOAD_DIR, FILE_PATH


def gen_token(prefix=None):
    """
    :param prefix:      str     前缀
    :return:            str     token值
    """
    token = prefix + uuid4().hex
    return token


def gen_token_movie_user():
    return gen_token(USER_TYPE_MOVIE)


def gen_token_admin_user():
    return gen_token(USER_TYPE_ADMIN)


def gen_token_cinema_user():
    return gen_token(USER_TYPE_CINEMA)


def filename_transfer(filename):
    """
    转换文件名称
    :param filename:        str                 原始文件名称
    :return:                tuple/(str, str)    (绝对路径， 相对路径)
    """
    filename = secure_filename(filename)
    suffix = filename.rsplit(".", 1)[-1]
    new_name = "{}.{}".format(uuid4().hex, suffix)
    abs_path = "{}/{}".format(UPLOAD_DIR, new_name)
    rel_path = "{}/{}".format(FILE_PATH, new_name)

    return abs_path, rel_path


def str_to_date(str_date):
    """
    字符串时间
    :param str_date:        str         字符串时间
    :return:                datetime    datetime 时间
    """
    return datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")


class GenEmailInfo:
    __str_obj = {
        "number": [48, 57],
        "lower_alpha": [65, 90],
        "upper_alpha": [97, 122],
        "special_str": ["\\", "_", "|", "-", "/"]
    }

    def __init__(self):
        self.str_pool = self.__gen_str_pool()

    def __to_chr(self, ords):
        """
        全部转换成ASCII对应的字符
        """
        if not isinstance(ords[0], int):
            return ords

        _start, _end = ords
        result = [chr(x) for x in range(_start, _end + 1)]
        return result

    def __gen_str_pool(self):
        str_pool = [self.__to_chr(x) for x in self.__str_obj.values()]
        lens = [len(y) for y in str_pool]
        len_max = max(lens)

        result = []
        for idx in range(len(lens)):
            tmp_len = lens[idx]
            cell_str = str_pool[idx]

            # 倍数，余数
            tmp_time, tmp_other = len_max // tmp_len, len_max % tmp_len
            tmp_str_pool = cell_str * tmp_time + cell_str[:tmp_other]
            result += tmp_str_pool
        return result

    def get_info(self, suffix, username, passwd_len, nbr):
        """
        生成邮箱注册信息
        :param suffix:          str/邮箱后缀，不包含@
        :param username:        str/用户名列表
        :param passwd_len:      int/密码长度
        :param nbr:             int/信息总数
        """

        suffix = suffix.replace("@", '')
        last_name = username + "-"
        qustion = "Nice name"

        result = []

        for count in range(1, nbr + 1):
            first_name = str(count)

            nickname = last_name + first_name
            password = "".join(sample(self.str_pool, passwd_len))
            email = nickname + "@" + suffix
            result.append([count, first_name, last_name, nickname, password, qustion, password, email])

        return result

    def to_excel(self, headers, title, data, file_name):
        """
        保存到excel
        :param headers:     list/tuple      标题
        :param title:       str             sheet名称
        :param data:        list            具体数据,[[], [], ..., []]
        :param file_name:   str             文件名称
        """
        # 生成一个 Workbook 的实例化对象，wb即代表一个 Excel 文件
        # 获取活跃的工作表，ws代表wb(工作簿)的一个工作表
        wb = Workbook()
        ws = wb.active
        ws.title = title

        # 写表头
        for i in range(len(headers)):
            upper_alpha = self.__to_chr(self.__str_obj["upper_alpha"])
            col_name = "{}{}".format(upper_alpha[i], 1)
            ws[col_name] = headers[i]

        for _data in data:
            ws.append(_data)

        suffix = ".xlsx"
        file_name = file_name.replace(suffix, '') + suffix
        save_path = file_name
        wb.save(save_path)
        print("[ {}, saved. ]".format(save_path))


def demo():
    username = "futureX"
    _suffix = "yandex.com"
    pass_len = 30
    nbr = 256

    headers = [
        "NO",
        "first_name",
        "last_name",
        "nickname",
        "password",
        "qustion",
        "password",
        "email"
    ]

    title = "yandex"
    file_name = "email_yandex"

    gei = GenEmailInfo()
    res = gei.get_info(_suffix, username, pass_len, nbr)

    gei.to_excel(headers, title, res, file_name)


if __name__ == "__main__":
    demo()
    pass
