"""
GIL（全局解释器锁）：
伪线程：
缺点：保证数据安全，效率降低

"""
from threading import Thread, Lock

number = 0


def task(lock):
    global number
    lock.acquire()  # 握住锁
    for i in range(100000):
        number += 1
    lock.release()  # 释放锁


if __name__ == '__main__':
    lock = Lock()
    t1 = Thread(target=task, name='1号窗口', args=(lock,))
    t2 = Thread(target=task, name='2号窗口', args=(lock,))
    t3 = Thread(target=task, name='3号窗口', args=(lock,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print('number:', number)
