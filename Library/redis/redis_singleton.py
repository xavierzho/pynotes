import threading
from redis import Redis, ConnectionPool


def synchronized(func):
    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return lock_func


class RedisConnectionPool(ConnectionPool):
    __instance = None

    @synchronized
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = ConnectionPool.__new__(cls)
        return cls.__instance


if __name__ == '__main__':
    conn_pool = RedisConnectionPool(max_connections=100, decode_responses=True,)
    conn = Redis(connection_pool=conn_pool)
    print(conn.get('name'))
