# coding=utf-8

from app.models import SmsSendRecord
from .. import db
import datetime


class SmsSendRecordRepository:
    @staticmethod
    def get_sms_info(phone_number,content,to_json=1):
        sms_info = SmsSendRecord.query.filter_by(phone_number=phone_number,content=content,used=0).first()

        if sms_info is not None and to_json == 1:
            sms_info = sms_info.to_json()

        return sms_info

    @staticmethod
    def add_sms(phone_number,content,template_code='SMS_143865884',result_code=''):
        sms_info = SmsSendRecord(phone_number,template_code,content,result_code)
        db.session.add(sms_info)
        db.session.commit()

        return True

    @staticmethod
    def up_sms(phone_number,content,used):
        sms_info = SmsSendRecord.query.filter_by(phone_number=phone_number,content=content,used=0).first()
        if sms_info is None:
            return False

        sms_info.used = used
        db.session.commit()

        return True

    @staticmethod
    def get_sms_count(phone_number,start_at='',end_at=''):
        if start_at == '':
            start_at = datetime.date.today()

        if end_at == '':
            end_at = start_at + datetime.timedelta(days=1)

        return SmsSendRecord.query.filter_by(phone_number=phone_number).\
            filter(SmsSendRecord.created_at.between(start_at,end_at)).count()
