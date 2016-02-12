import redis


class RedisConnection:

    def __init__(self, host, port):
        self.conn = redis.StrictRedis(host=host, port=port, db=0)
        self.insertId = 0

    def set(self, value):
        self.insertId += 1
        self.conn.set(self.insertId, value)
        return self.insertId

    def get(self, id):
        return self.conn.get(id)
