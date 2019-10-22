# coding=utf-8

from .import api
from flask import request
from ..Utils.Utils import response,check_phone
from ..Enums.ResponseEnum import ResponseCodeEnum
from ..Services.SmsService import SmsService
from ..Services.SmsSendRecordService import SmsSendRecordService
import random
from config import SmsLimitCount
from .authentication import mini_authorize
import json


# 发送短信
@api.route('/send_sms', methods=['POST'])
@mini_authorize
def send_sms():
    param = request.json

    phone_number = param.get('phone_number','')
    if phone_number == '':
        return response(None,ResponseCodeEnum.miss_param,'手机号不能为空')

    if not check_phone(phone_number):
        return response(None,ResponseCodeEnum.error_param,'手机号格式错误')

    sms_count = SmsSendRecordService.get_sms_count(phone_number)

    if sms_count >= SmsLimitCount:
        return response(None, ResponseCodeEnum.fail, '今天短信达到上限')

    code = random.randint(1000, 9999)
    template_code = 'SMS_143865884'
    return_code = SmsService.send_sms(phone_number, code,template_code)

    result = SmsSendRecordService.add_sms(phone_number,code,template_code,return_code)
    if not result:
        return response(None,ResponseCodeEnum.fail,'入库失败')

    result = json.loads(return_code)
    if 'Code' not in result.keys() or result['Code'] != 'OK':
        return response(None,ResponseCodeEnum.fail,'发送失败')

    return response()


# 校验短信
@api.route('/check_sms', methods=['POST'])
@mini_authorize
def check_sms():
    param = request.json

    phone_number = param.get('phone_number','')
    code = param.get('code','')
    if phone_number == '' or code == '':
        return response(None,ResponseCodeEnum.miss_param,'手机号或验证码不能为空')

    if not check_phone(phone_number):
        return response(None,ResponseCodeEnum.error_param,'手机号格式错误')

    result = SmsSendRecordService.check_code(phone_number,code)
    if not result:
        return response(None,ResponseCodeEnum.fail,'验证码错误或者已过期')

    return response()



