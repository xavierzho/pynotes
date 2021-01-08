import time
from threading import Lock, Thread, current_thread


ticket = 10


def sale_ticket(lock):
    global ticket
    while True:
        lock.acquire(timeout=1.5)
        if ticket > 0:
            print('{}正在卖第{}张票'.format(current_thread().name, ticket))
            ticket -= 1
            time.sleep(0.5)

        else:
            print('票卖完了！')

            break
        lock.release()


if __name__ == '__main__':
    lock = Lock()

    t1 = Thread(target=sale_ticket, name='1号窗口', args=(lock,))
    t2 = Thread(target=sale_ticket, name='2号窗口', args=(lock,))
    t3 = Thread(target=sale_ticket, name='3号窗口', args=(lock,))
    t4 = Thread(target=sale_ticket, name='4号窗口', args=(lock,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

