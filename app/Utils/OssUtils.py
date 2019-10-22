#coding=utf-8

import oss2
from config import AccessKeyId,AccessKeySecret,EndPoint,Bucket


class OssUtils(object):
    def __init__(self):
        # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
        auth = oss2.Auth(AccessKeyId, AccessKeySecret)
        # Endpoint以杭州为例，其它Region请按实际情况填写。
        self.bucket = oss2.Bucket(auth, EndPoint, Bucket)

    def put_object_from_file(self,target_url,local_url):
        try:
            self.bucket.put_object_from_file(target_url,local_url)
            url = self.get_object_url(target_url)
        except Exception as e:
            print(e)
            url = ''

        return url

    def get_object_url(self, target_url):
        return 'https://' + Bucket + '.' + EndPoint + '/' + target_url