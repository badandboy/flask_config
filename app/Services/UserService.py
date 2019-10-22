# coding=utf-8

from ..Repositories.UserRepository import UserRepository


class UserService:
    @staticmethod
    def get_user_info(user_id):
        user_info = UserRepository.get_user_info(user_id)

        return user_info

    @staticmethod
    def edit_user(user_id,data):
        return UserRepository.edit_user(user_id, data)

    @staticmethod
    def login(user_name,user_password):
        return UserRepository.login(user_name, user_password)
