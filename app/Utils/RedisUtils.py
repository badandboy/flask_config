#!/usr/bin/python
#coding=utf-8

from redis import Redis, ConnectionPool

from config import REDIS_CONF,EXPIRES_TIME


pool = ConnectionPool(host=REDIS_CONF['host'], port=REDIS_CONF['port'], password=REDIS_CONF['password'], db=REDIS_CONF['db'])


class TRedisDB(object):
    def __init__(self):
        self.db = Redis(connection_pool=pool)

    def set(self, key, value):
        return self.db.set(key, value)

    def setnx(self, key, value):
        return self.db.setnx(key, value)

    def setex(self, key, value, time=EXPIRES_TIME):
        return self.db.setex(key, time, value)

    def get_data(self, redis_key):
        return self.db.get(redis_key)
