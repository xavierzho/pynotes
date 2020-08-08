"""
共享数据：
如果有全局变量，则每个线程是共享的。
python中多线程跟阻塞时间、运算量来

"""

import time
from threading import Thread, current_thread

ticket = 10


def sale_ticket():
    global ticket
    while True:
        if ticket > 0:
            print('{}正在卖第{}张票！'.format(current_thread().name, ticket))
            ticket -= 1
            time.sleep(0.5)
        else:
            break


if __name__ == '__main__':
    t1 = Thread(target=sale_ticket, name='1号窗口')
    t2 = Thread(target=sale_ticket, name='2号窗口')
    t3 = Thread(target=sale_ticket, name='3号窗口')

    t1.start()
    t2.start()
    t3.start()
