#coding=utf-8
from flask import Blueprint


#配置蓝本
director_api=Blueprint('director_api',__name__)


#初始化自定义模块，否则路由无法找到相对应的模块


from . import director
