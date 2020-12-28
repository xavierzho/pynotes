"""
@Author: Jonescyna@gmail.com
@Created: 2020/12/23
"""
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} running time:{start_time - end_time} secs")
        return res

    return wrapper


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 27, 28, 29, 30, 34, 39, 42]


def cut_rod_rec(p, n):  # rec=recursion
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_rec(p, i) + cut_rod_rec(p, n - i))
        return res


def cut_rod_rec_2(p, n):
    # 以下两行代码相当于 p[0]
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_rec_2(p, n - i))
        return res


@cal_time
def test():
    return cut_rod_rec(p, 9)


@cal_time
def test2():
    return cut_rod_rec_2(p, 9)


@cal_time
def cut_rod_dp(p, n):
    r = [0 for _ in range(n + 1)]  # 最终收益的列表
    for i in range(1, n + 1):  #
        res = 0
        for j in range(1, i + 1):  # 计算所有情况的最大值
            res = max(res, p[j] + r[i - j])
        r[i] = res
    return r[n]


def cut_rod_extend(p, n):
    r = [0 for _ in range(n + 1)]
    s = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        price = 0  # 价格最优解
        program = 0  # 价格最优对应的方案的左边不切割的部分的长度
        for j in range(1, i + 1):
            if p[j] + r[i - j] > price:
                price = p[j] + r[i - j]
                program = j
        r[i] = price
        s[i] = program
    # print(r)
    return r[n], s


def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    ams = []
    while n > 0:
        ams.append(s[n])  # 将不切割的部分保存起来
        n -= s[n]
    return ams


print(cut_rod_solution(p, 9))
