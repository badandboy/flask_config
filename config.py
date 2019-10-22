# coding=utf-8
import os
from ConfigUtils import ConfigUtils


conf = ConfigUtils()
cf = conf.get_config()

basedir = os.path.dirname(os.path.abspath(__file__))
base = os.path.join(basedir,'images')

serverPort = 5000

# 个人模式
appid = cf.get('MiniProgram','appid')
appsercret = cf.get('MiniProgram','appsercret')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF','mp4','mp4','AVI','flash','wma'])
EXPIRES_TIME = 86400

# 短信服务配置
SmsAccessKeyId = cf.get('Sms','SmsAccessKeyId')
SmsAccessKeySecret = cf.get('Sms','SmsAccessKeySecret')
SmsEndPoint = cf.get('Sms','SmsEndPoint')
SmsLimitCount = cf.get('Sms','SmsLimitCount')

# 阿里云oss配置
AccessKeyId = cf.get('OSS','AccessKeyId')
AccessKeySecret = cf.get('OSS','AccessKeySecret')
EndPoint = cf.get('OSS','EndPoint')
Bucket = cf.get('OSS','Bucket')

# 接口请求日志开关
logSwitch = cf.get('Log','LogSwitch')


class Config:
    ENV = cf.get('Flask','ENV')
    DEBUG = cf.get('Flask','DEBUG')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_DATABASE_URI ="mysql+pymysql://"+cf.get('Database','username')+":"+cf.get('Database','password')+"@"+cf.get('Database','host')+":"+cf.get('Database','port')+"/limanet?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    @staticmethod
    def init_app(app):
        pass

# redis配置
REDIS_CONF = {
    'host': cf.get('Redis','host'),
    'port': cf.get('Redis','port'),
    'db': cf.get('Redis','db'),
    'password': cf.get('Redis','password')
}