# coding=utf-8

from app.models import User
from .. import db


class UserRepository:
    @staticmethod
    def get_user_info(user_id):
        user_info = User.query.filter_by(user_id=user_id).first()

        if user_info is not None:
            user_info = user_info.to_json()

        return user_info

    @staticmethod
    def edit_user(user_id, data):
        wx_user = User.query.filter_by(user_id=user_id).update(data)
        db.session.commit()

        return wx_user

    @staticmethod
    def login(user_name,user_password):
        user_info = User.query.filter_by(user_name=user_name,user_password=user_password).first()

        if user_info is not None:
            user_info = user_info.to_json()

        return user_info
