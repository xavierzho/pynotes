"""
死锁：
    两把锁
    申请锁的顺序使用不当
开发过程中使用线程， 在线程间共享多个资源的时候，
如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。
尽管死锁很少发生，但是一旦发生就会造成应用的停止响应，程序不做任何事情

避免死锁：
1.重构代码
2.使用timeout参数

"""
import time
from threading import Lock, Thread, current_thread


def task1(lock1, lock2):
    lock1.acquire()
    print('获取到lock1锁。。。')
    for i in range(5):
        print('--->', i)
        time.sleep(0.01)
    if lock2.acquire(timeout=2):
        print('{}获取到lock1，lock2锁'.format(current_thread().name))
        lock2.release()
    lock1.release()


def task2(lock2, lock1):
    lock2.acquire()
    print('获取到lock2锁。。。')
    for i in range(5):
        print('{}--->{}'.format(current_thread().name, i))
        time.sleep(0.01)
    if lock1.acquire(timeout=2):
        print('{}获取到lock1，lock2锁'.format(current_thread().name))
        lock1.release()
    lock2.release()


if __name__ == '__main__':
    lock1 = Lock()
    lock2 = Lock()

    t1 = Thread(target=task1, args=(lock1, lock2))
    t2 = Thread(target=task2, args=(lock2, lock1))

    t1.start()
    t2.start()
