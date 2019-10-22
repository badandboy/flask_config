# encoding utf-8
from flask import Flask
from config import base,REDIS_CONF,Config
from flask_uploads import configure_uploads, UploadSet
from flask_sqlalchemy import SQLAlchemy
import redis
import os

db = SQLAlchemy()
pool = redis.ConnectionPool(host=REDIS_CONF['host'],password=REDIS_CONF['password'],port=REDIS_CONF['port'],db=REDIS_CONF['db'])
r = redis.Redis(connection_pool=pool)


def create_app():
    #...
    app=Flask(__name__,template_folder='./template/360network/dist',static_folder="./template/360network/dist/static")
    app.config['UPLOADS_DEFAULT_DEST'] = base
    photo = UploadSet()
    configure_uploads(app, photo)
    app.config.from_object(Config)
    Config.init_app(app)
    db.init_app(app)
    from .api_1_0 import api as api_1_0_blueprint
    from .index import director_api as director_api
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')
    app.register_blueprint(director_api, url_prefix='')

    return app

