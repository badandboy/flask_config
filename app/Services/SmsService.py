# coding=utf-8

from ..Repositories.SmsRepository import SmsRepository


class SmsService:
    @staticmethod
    def send_sms(phone_number,content,template_code='SMS_143865884'):
        result = SmsRepository.send_sms(phone_number,content,template_code)

        return result


