"""
@Author: Jonescyna@gmail.com
@Created: 2020/12/22
"""


# 递归存在子问题重复计算
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))
