import time
from multiprocessing import Process
from proxyPool.free_proxies.api import app
from proxyPool.free_proxies.getter import Getter
from proxyPool.free_proxies.tester import Tester
from proxyPool.free_proxies.db import RedisClient
from proxyPool.free_proxies.settings import *


class Scheduler:
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        :param cycle:
        :return:
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        :param cycle:
        :return:
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self, cycle=API_CYCLE):
        """
        开启API
        :param cycle:
        :return:
        """
        app.run(API_HOST, API_PORT)

    def schedule_db(self, cycle=DB_CYCLE):
        """
        运行redis数据库
        :param cycle:
        :return:
        """
        db = RedisClient()
        while True:
            print('redis正在运行')
            print(db)
            time.sleep(cycle)

    def run(self):
        print('代理池开始运行')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()

        if DB_ENABLED:
            db_process = Process(target=self.schedule_db)
            db_process.start()
