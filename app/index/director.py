# coding=utf-8
from .import director_api
from flask import Flask,render_template


# 获取活动列表
@director_api.route('/')
def index():
    return render_template('index.html')