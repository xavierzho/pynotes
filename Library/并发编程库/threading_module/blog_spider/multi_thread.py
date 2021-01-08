"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/5
"""
import threading
import single_thread
import time


def cal_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print(f"{func.__name__}：{time.time() - start}s")
        return ret

    return inner


@cal_time
def s_thread():
    print("single thread start")
    for url in single_thread.urls:
        single_thread.craw(url)
    print("single thread end")


@cal_time
def m_thread():
    print("multi thread start!")
    threads = []
    for url in single_thread.urls:
        threads.append(threading.Thread(target=single_thread.craw, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print("multi thread end!")


if __name__ == '__main__':
    s_thread()
    m_thread()
