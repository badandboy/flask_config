# -*- coding: utf-8 -*-

from flask import jsonify
from ..Enums.ResponseEnum import ResponseCodeEnum,ResponseMsgEnum
import re
import random


# 返回参数封装,小程序使用
def response(data=None, code=ResponseCodeEnum.success, msg=None):
    if msg is None and code in ResponseMsgEnum.keys():
        msg = ResponseMsgEnum[code]

    return jsonify({
        "code": code,
        "msg": msg,
        "data": data
    })


# 检测手机号是否合法
def check_phone(phone_number):
    return re.match(r"^1[35678]\d{9}$", phone_number)


# 获取随机字符串
def getRandString(prefix='str_', length=16):
    character = 'abcdefghijklmnopqrstuvwxyz0123456789'

    result = ''
    while len(result) < int(length):
        rand = random.randint(0,33)
        result += character[rand:rand+1]

    return prefix+result



