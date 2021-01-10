import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} running time:{start_time - end_time} secs")
        return res
    return wrapper
