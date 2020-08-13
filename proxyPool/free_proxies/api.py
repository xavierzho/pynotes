from flask import Flask, g
from proxyPool.free_proxies.db import RedisClient

__all__ = ['app']
app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h1>Welcome to Proxy Pool System</h1>'


@app.route('/random')
def get_proxy():
    """
    get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()


@app.route('/count')
def get_counts():
    """
    get the count of proxies
    :return:
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run()
