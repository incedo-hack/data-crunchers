import redis
from settings import *


class Redis:
    def __init__(self):
        self.host = redis_host
        self.port = redis_port
        self.db = redis_db

    def connect(self):
        return redis.StrictRedis(host=self.host, port=self.port, db=self.db)

    @staticmethod
    def addin_hash(connection, name, key, value):
        return connection.hset(name, key, value)

    @staticmethod
    def getfrom_hash(connection, name, key):
        return connection.hget(name, key)