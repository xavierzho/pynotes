import time


# 9_装饰器
def calculate_time(f):
    def inner(*args, **kwargs):
        start_time = time.time()
        ret = f(*args, **kwargs)  # f1() f2()
        end_time = time.time()
        print(end_time - start_time)
        return ret
    return inner


@calculate_time  # inner = calculate_time(inner)
def add(m, n, x):
    time.sleep(2)
    return m + n + x


print(add(1, 2, 5))
