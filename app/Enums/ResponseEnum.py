# coding=utf-8


# 小程序返回状态码
class ResponseCodeEnum(object):
    success = 0 #请求成功,
    fail = 1  #请求失败,

    no_auth = -1000  #没有权限
    unknown_error = -1001  #未知错误

    miss_param = 1001  #缺少参数
    error_param = 1002  #参数错误
    db_empty = 1003  #数据库不存在

    user_not_exist = 2001  #用户不存在


# 小程序返回错误信息
ResponseMsgEnum = {
    ResponseCodeEnum.success: '请求成功',
    ResponseCodeEnum.fail: '请求失败',

    ResponseCodeEnum.no_auth: '请求不合法',
    ResponseCodeEnum.unknown_error: '未知错误',

    ResponseCodeEnum.miss_param: '缺少参数',
    ResponseCodeEnum.error_param: '参数错误',
    ResponseCodeEnum.db_empty: '数据不存在',

    ResponseCodeEnum.user_not_exist: '用户不存在',
}