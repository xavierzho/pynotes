"""
线程的信号量
 count  5
 信号量的实现方式：
在内部有一个counter计数器，每当我们s.acquire()一次，计数器将进行减1处理
每当s.release()一次，计数器将进行加1处理，每当激素去为0的时候其他线程就处于等待状态
counter的值就是同一时间可以开启线程的数量

建议用with

"""
import time
from threading import Thread, Semaphore, current_thread


def task(s):
    # s.acquire()  # 减1
    with s:
        for i in range(5):
            print('{}扫地中...{}'.format(current_thread().name), i)
            time.sleep(1)
    # s.release()  # 加1


if __name__ == '__main__':
    s = Semaphore(4)
    for i in range(10):
        t = Thread(target=task, args=(s,))
        t.start()
