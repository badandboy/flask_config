# coding=utf-8

from .import api
from flask import request,jsonify,make_response
import datetime,random
from config import basedir, ALLOWED_EXTENSIONS
import os
from .authentication import authorize
from ..Utils.OssUtils import OssUtils
from ..Utils.Utils import getRandString


# 文件名唯一
class Pic_str:
    def create_uuid(self):
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        randomNum = random.randint(0, 100)
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        return uniqueNum


# 上传文件的类型
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 上传文件
@api.route('/uploadAvatar',methods=['POST'])
@authorize
def uploadAvatar():
    file_dir = os.path.join(basedir,'static/photo')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
        # f = request.files['photo']
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

    f = request.files['file']

    if f and allowed_file(f.filename):
        fname = f.filename
        ext = fname.rsplit('.', 1)[1]
        new_filename = Pic_str().create_uuid() + '.' + ext
        file_path = os.path.join(file_dir, new_filename)
        f.save(file_path)

        oss_obj = OssUtils()
        target_url = datetime.datetime.now().strftime("%Y%m%d") + '_' + getRandString('', 16) + '.' + ext
        url = oss_obj.put_object_from_file(target_url,file_path)

        if os.path.exists(file_path):
            os.remove(file_path)

        return jsonify({"code":"200","message":"上传成功","url":url})
    else:
        return jsonify({"code":"400","message":"上传失败"})


#照片预览
@api.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = os.path.join(basedir,'static/photo/')
    filename_url = file_dir+filename
    if request.method == 'GET':
        if filename is None:
            return jsonify({"code":"401","message":"参数缺失"})
        else:
            if os.path.exists(filename_url):
                image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
                response = make_response(image_data)
                print(image_data,response)
                response.headers['Content-Type'] = 'image/png'
                return response

            else:
                filename = '20190714015117.jpg'
                image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
                response = make_response(image_data)
                response.headers['Content-Type'] = 'image/png'
                return response
    else:
        pass