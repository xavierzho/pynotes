"""
自定义线程：
    1.定义一个类继承Thread
    2.重写：[__init__]  必须重写：run()
    3.创建线程类对象
    4.启动线程
"""
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(5):
            print('{}正在打印:{}'.format(self.name, i))
            time.sleep(0.1)


if __name__ == '__main__':
    t1 = MyThread('小明')
    t2 = MyThread('小花')
    t3 = MyThread('zxq')

    t1.start()
    t2.start()
    t3.start()
