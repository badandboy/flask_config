# coding=utf-8

from . import api
from flask import request
from flask_cors import cross_origin
from .. import r
from ..Utils.Utils import response
from ..Enums.ResponseEnum import ResponseCodeEnum
import time, hmac, base64
from config import EXPIRES_TIME,appid
from .authentication import authorize
from ..Services.UserService import UserService


# 生成token
def generate_token(key, expire=3600):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest()
    token = ts_str+':'+sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")


# 存redis
def set_redis_data(conn,key, value):
    data = value
    conn.set(
        name=key,
        value=data,
        ex=EXPIRES_TIME
    )


# 删除redis
def delete_redis_data(conn,key):
        try:
            conn.delete(key)
            return True
        except:
            return False


# 登录验证
@api.route('/login',methods=['POST'])
@cross_origin()
def login():
    params = request.form

    username = params.get('username')
    password = params.get('password')

    if username is None or password is None:
        return response(None,ResponseCodeEnum.miss_param)

    password = base64.b64encode(password.encode('utf-8')).decode("utf-8")
    user_info = UserService.login(username,password)

    if user_info is None:
        return response(None,ResponseCodeEnum.db_empty,'用户名或密码不对')

    token = generate_token(username)
    set_redis_data(r, token, user_info['user_id'])

    return response(token)


# 更新密码
@api.route('/updatePassword',methods=['POST'])
@authorize
def updatePassword():
    param = request.form
    password = param.get('password')

    if password is None:
        return response(None,ResponseCodeEnum.miss_param,'密码不能为空')

    token = request.headers.get("token")
    user_id = r.get(token)

    password = base64.b64encode(password.encode('utf-8')).decode("utf-8")

    data = {
        'user_password': password
    }

    UserService.edit_user(user_id, data)

    return response()


# 登出
@api.route('/login_out',methods=['POST'])
@authorize
def loginOut():
    param = request.json
    token = param["token"]

    res = delete_redis_data(r,token)

    if res:
        return response()
    else:
        return response(None,ResponseCodeEnum.fail,'退出失败')
