# coding=utf-8

from flask import request
from .. import r
from functools import wraps
from ..Utils.Utils import response
from ..Enums.ResponseEnum import ResponseCodeEnum


#获取token
def authorize(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = request.headers.get("token")
        if token is None:
            return response(None,ResponseCodeEnum.no_auth)

        user_id = r.get(token)
        if user_id:
            try:
                return fn(*args, **kwargs)#登录了就返回请求
            except Exception as e:
                return response(None, ResponseCodeEnum.unknown_error)

    return wrapper
