"""
进程池(pool):
    减少资源创建
"""
import os
import time
from multiprocessing import Pool, Manager


def task1():
    print('洗衣服：', i, os.getpid(), os.getppid())
    time.sleep(0.5)
    return '我是进程' + str(os.getpid())


def callBack(msg):
    print('{}洗衣服任务完成！'.format(msg))


if __name__ == '__main__':
    queue = Manager().Queue()
    pool = Pool(4)
    # 非阻塞式
    for i in range(10):
        pool.apply_async(task1, callback=callBack)
        # 阻塞式
        # pool.apply(task1)
        
    # 添加任务结束
    pool.close()
    # 阻塞主进程
    pool.join()

    print('main_over:')
