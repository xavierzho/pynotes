"""
@Author: Jonescyna@gmail.com
@Created: 2020/12/22
"""


def fibonacci(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


print(fibonacci(100))

