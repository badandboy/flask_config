# coding=utf-8

from ..Repositories.SmsSendRecordRepository import SmsSendRecordRepository
import datetime


class SmsSendRecordService:
    @staticmethod
    def get_sms_info(phone_number,content):
        sms_info = SmsSendRecordRepository.get_sms_info(phone_number,content)

        return sms_info

    @staticmethod
    def add_sms(phone_number,content,template_code='SMS_143865884',result_code=''):
        result = SmsSendRecordRepository.add_sms(phone_number,content,template_code,result_code)

        return result

    @staticmethod
    def up_sms(phone_number,content,used):
        result = SmsSendRecordRepository.up_sms(phone_number,content,used)

        return result

    @staticmethod
    def check_code(phone_number,code):
        sms_info = SmsSendRecordRepository.get_sms_info(phone_number,code,0)
        if sms_info is None:
            return False

        now_time = datetime.datetime.now()
        expired_at = sms_info.created_at + datetime.timedelta(minutes=5)

        if expired_at < now_time:
            return False

        # 用过了不能再用了
        SmsSendRecordRepository.up_sms(phone_number,code,1)

        return True

    @staticmethod
    def get_sms_count(phone_number,start_at='',end_at=''):
        return SmsSendRecordRepository.get_sms_count(phone_number,start_at,end_at)
