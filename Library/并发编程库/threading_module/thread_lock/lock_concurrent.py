"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/6
"""
import threading
import time

lock = threading.Lock()


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    with lock:
        if account.balance >= amount:

            print(f'{threading.current_thread().name},取钱成功')
            account.balance -= amount
            print(f"{threading.current_thread().name},余额{account.balance}")

        else:
            print(f'{threading.current_thread().name},取钱失败余额不足！')


if __name__ == '__main__':
    account = Account(1000)
    t1 = threading.Thread(name='t1', target=draw, args=(account, 800))
    t2 = threading.Thread(name='t2', target=draw, args=(account, 800))
    t1.start()
    t2.start()
