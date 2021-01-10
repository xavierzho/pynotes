import asyncio
import aiohttp
import time
import sys

try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
from proxyPool.free_proxies.db import RedisClient
from proxyPool.free_proxies.settings import *

VALID_STATUS_CODES = [200]
TEST_URL = 'http://www.baidu.com'
BATCH_TEST_SIZE = 100


# DAO:database access object
class Tester(object):
    def __init__(self):
        self.redis = RedisClient()

    async def text_single_proxy(self, proxy):
        """
        测试单个代理
        :param proxy: 代理
        :return:
        """
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                # real_proxy2 = 'https://' + proxy
                print('正在测试', proxy)
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        print('代理可用', proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('请求响应码不符合要求', response.status, 'IP', proxy)

            except (
                    ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.ThreadedChildWatcher,
                    AttributeError):
                self.redis.decrease(proxy)
                print('代理请求失败', proxy)

    def run(self):
        """
        测试主函数
        :return:
        """
        print('测试器开始运行')
        try:
            count = self.redis.count()
            print('当前剩余', count, '个代理')
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                stop = min(i + BATCH_TEST_SIZE, count)
                print('正在测试第', start + 1, '-', stop, '个代理')
                test_proxies = self.redis.batch(start, stop)
                loop = asyncio.get_event_loop()
                tasks = [self.text_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误', e.args)
