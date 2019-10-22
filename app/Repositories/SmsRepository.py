# coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from config import SmsAccessKeyId,SmsAccessKeySecret,SmsEndPoint


class SmsRepository:
    @staticmethod
    def send_sms(phone_number,content,template_code='SMS_143865884'):
        client = AcsClient(SmsAccessKeyId, SmsAccessKeySecret, SmsEndPoint)

        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')  # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers', phone_number)
        request.add_query_param('SignName', "港盛国际")
        request.add_query_param('TemplateCode', template_code)
        request.add_query_param('TemplateParam', {'code':content})

        response = client.do_action_with_exception(request)
        response = str(response, encoding='utf-8')

        return response


