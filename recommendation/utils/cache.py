import redis


class Redis:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 6379
        self.db = 0

    def connect(self):
        return redis.StrictRedis(host=self.host, port=self.port, db=self.db)

    @staticmethod
    def addin_hash(connection, name, key, value):
        return connection.hset(name, key, value)

    @staticmethod
    def getfrom_hash(connection, name, key):
        return connection.hget(name, key)