import configparser
import os


class ConfigUtils:
    def __init__(self):
        env = os.getenv('FLASK_ENV')
        if env == 'production':
            config_path = os.path.join(os.path.abspath('.'), "production.ini")
        else:
            config_path = os.path.join(os.path.abspath('.'), "develop.ini")

        self.cf = configparser.ConfigParser()
        self.cf.read(config_path,'utf8')  # 读取配置文件

    def get_config(self):
        return self.cf

