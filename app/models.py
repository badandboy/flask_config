# coding=utf-8
from . import db
from datetime import datetime
import json


# 后台用户表
class User(db.Model):
    __tablename__ =  't_user'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64),  unique=True,nullable=False)
    user_name = db.Column(db.String(255))
    user_password = db.Column(db.String(255))

    def to_json(self):
        json = {
            'id': self.id,
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_password': self.user_password
        }
        return json


# 活动管理
class Activity(db.Model):
    __tablename__ = 't_activity'
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.String(64),nullable=False )
    title = db.Column(db.String(64), nullable=False)
    patch_img_url = db.Column(db.String(64), nullable=False)
    content_url = db.Column(db.String(256), nullable=False)
    poster_url = db.Column(db.String(256), nullable=False)
    enroll_start_at = db.Column(db.DateTime, nullable=False)
    enroll_stop_at = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(4), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, activity_id, title, patch_img_url, content_url,poster_url, enroll_start_at, enroll_stop_at, status):
        self.activity_id = activity_id
        self.title = title
        self.patch_img_url = patch_img_url
        self.content_url = content_url
        self.poster_url=poster_url
        self.enroll_start_at = enroll_start_at
        self.enroll_stop_at = enroll_stop_at
        self.state = 0
        self.status = status

    def to_json(self):
        json = {
            'activity_id': self.activity_id,
            'title': self.title,
            'patch_img_url': self.patch_img_url,
            'content_url': self.content_url,
            'poster_url':self.poster_url,
            'enroll_start_at': self.enroll_start_at.strftime('%Y-%m-%d %H:%M:%S') if self.enroll_start_at else '',
            'enroll_stop_at': self.enroll_stop_at.strftime('%Y-%m-%d %H:%M:%S') if self.enroll_stop_at else '',
            'state': self.state,
            'status': self.status,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S')

        }

        return json


# 短信发送记录
class SmsSendRecord(db.Model):
    __tablename__ = 't_sms_send_record'
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(20), nullable=False)
    template_id = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    used = db.Column(db.Integer, nullable=True)
    return_code = db.Column(db.String(256), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, phone_number, template_id, content,return_code):
        self.phone_number = phone_number
        self.template_id = template_id
        self.content = content
        self.return_code = return_code
        self.used = 0
        self.created_at = datetime.now()


    def to_json(self):
        json = {
            'id': self.id,
            'phone_number': self.phone_number,
            'template_id': self.template_id,
            'content': self.content,
            'used': self.used,
            'return_code': self.return_code,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

        return json










