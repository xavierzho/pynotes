"""
pyhton 如何创建一个线程
    线程：
    1. t1 = Thread(target=task1)
    2.自定义线程

    run()
    start()
    join()
    name:默认的Thread-1,Thread-2....
    
"""
import time
import os
from threading import Thread, current_thread


def task1():
    for i in range(5):
        print("{}洗衣服:".format(current_thread().name), i, os.getpid(), os.getppid())
        time.sleep(0.5)


def task2(n):
    for i in range(n):
        print('{}劳动最光荣，扫地中。。。'.format(current_thread().name), i, os.getpid(), os.getppid())
        time.sleep(0.5)


if __name__ == '__main__':
    print('main:', os.getpid())
    # 创建线程对象
    t1 = Thread(target=task1, name='警察')
    t2 = Thread(target=task2, name='小偷', args=(6,))

    # 线程启动
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    for i in range(3):
        if t1.is_alive():
            print('main:', i)

