#coding=utf-8
from flask import Blueprint

#配置蓝本
api = Blueprint('api',__name__)

from . import upload,activity,login


