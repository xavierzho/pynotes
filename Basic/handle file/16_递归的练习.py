# 使用递归算法，计算阶乘


def factorial(a):
    if a == 1:
        return a
    else:
        return a * factorial(a - 1)


a = int(input("请输入一个需要算阶乘的数"))

print(factorial(a))
