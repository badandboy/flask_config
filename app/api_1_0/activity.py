# coding=utf-8

from flask import request
from app.models import Activity
from .import api
from ..Utils.Utils import response,getRandString
from ..Enums.ResponseEnum import ResponseCodeEnum
from .. import db
from .authentication import authorize


# 获取活动列表
@api.route('/get_activity_list', methods=['POST'])
@authorize
def get_activity_list():
    param = request.json

    page_index = int(param.get('page_number', 1))
    page_size = int(param.get('page_size', 10))

    pagination = Activity.query.filter_by(state=0).order_by(Activity.id.desc()).paginate(page_index,page_size,error_out=False)

    total = pagination.total
    activities = pagination.items

    list = [activity.to_json() for activity in activities]

    result = {"total": total, "list": list}

    return response(result)


# 获取活动详情
@api.route('/get_activity_detail', methods=['POST'])
@authorize
def get_activity_detail():
    param = request.json

    activity_id = param.get('activity_id')
    if activity_id is None:
        return response(None, ResponseCodeEnum.miss_param)

    # 获取记录
    activity = Activity.query.filter_by(activity_id=activity_id, state=0).first()
    if activity is None:
        return response(None, ResponseCodeEnum.db_empty)

    activity = activity.to_json()

    return response(activity)


# 增加活动列表
@api.route('/add_activity', methods=['POST'])
@authorize
def add_activity():
    param = request.json
    title = param.get('title')
    patch_img_url = param.get('patch_img_url')
    content_url = param.get('content_url')
    poster_url = param.get('poster_url')
    enroll_start_at = param.get('enroll_start_at')
    enroll_stop_at = param.get('enroll_stop_at')
    status = param.get('status')

    if title is None:
        return response(None, ResponseCodeEnum.miss_param)

    activity_id = getRandString('ac_', 16)
    activity = Activity(activity_id, title, patch_img_url, content_url, poster_url,enroll_start_at, enroll_stop_at,status)
    db.session.add(activity)
    db.session.commit()

    return response()


# 编辑活动
@api.route('/edit_activity', methods=['POST'])
@authorize
def edit_activity():
    param = request.json

    activity_id = param.get('activity_id')
    title = param.get('title')
    patch_img_url = param.get('patch_img_url')
    content_url = param.get('content_url')
    poster_url = param.get('poster_url')
    enroll_start_at = param.get('enroll_start_at')
    enroll_stop_at = param.get('enroll_stop_at')
    status = param.get('status', 1)

    if activity_id is None or title is None or patch_img_url is None or content_url is None or poster_url is None or \
            enroll_start_at is None or enroll_stop_at is None:
        return response(None, ResponseCodeEnum.miss_param)

    activity_info = Activity.query.filter_by(activity_id=activity_id,state=0).first()
    if activity_info is None:
        return response(None, ResponseCodeEnum.db_empty)

    activity_info.title = title
    activity_info.patch_img_url = patch_img_url
    activity_info.content_url = content_url
    activity_info.poster_url = poster_url
    activity_info.enroll_start_at = enroll_start_at
    activity_info.enroll_stop_at = enroll_stop_at
    activity_info.status = status

    db.session.commit()

    return response()


# 删除活动
@api.route('/del_activity', methods=['POST'])
@authorize
def del_activity():
    param = request.json

    activity_id = param.get('activity_id')
    if activity_id is None:
        return response(None, ResponseCodeEnum.miss_param)

    # 获取记录
    activity = Activity.query.filter_by(activity_id=activity_id, state=0).first()

    if activity is None:
        return response(None, ResponseCodeEnum.db_empty)

    activity.state = 1
    db.session.commit()

    return response()


# 关闭活动
@api.route('/close_activity', methods=['POST'])
@authorize
def close_activity():
    param = request.json

    activity_id = param.get('activity_id')
    if activity_id is None:
        return response(None, ResponseCodeEnum.miss_param)

    # 获取记录
    activity = Activity.query.filter_by(activity_id=activity_id, state=0).first()

    if activity is None:
        return response(None, ResponseCodeEnum.db_empty)

    activity.status = 1
    db.session.commit()

    return response()