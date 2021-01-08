"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/6
"""
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing.pool import Pool


# PRIMES = [112272535095293] * 100
PRIMES = [112272535095293] * 50


def cal_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print(f"{func.__name__}：{time.time() - start}s")
        return ret

    return inner


def is_prime(number):
    """判断是否为素数"""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    sqrt_num = int(math.floor(math.sqrt(number)))
    for i in range(3, sqrt_num + 1, 2):
        if number % i == 0:
            return False
    return True


@cal_time
def single_thread():
    for num in PRIMES:
        is_prime(num)


@cal_time
def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


@cal_time
def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


@cal_time
def multi_processing():
    pool = Pool(4)
    for i in PRIMES:
        res = pool.apply_async(is_prime, (i,))
        print(res.ready())
        # pool.apply(is_prime, (i,))
    # pool.map_async(is_prime, PRIMES)
    pool.close()
    pool.join()


if __name__ == '__main__':
    # single_thread()
    # multi_thread()
    # multi_process()
    multi_processing()
