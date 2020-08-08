# 解释出栈入栈的顺序，先进后出，后进先出
def test01(n):
    print("test01:", n)
    if n == 0:
        print("over")
    else:
        test01(n - 1)
    print("test01***", n)


def test02():
    print("test02")


test01(4)


# 递归函数，计算阶乘

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)

print(result)
# 分形几何？

# 斐波那契数列 F（n）= F（n-1）+F（n-2）


def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)


print(f(6))

# 汉诺塔问题

count = 0


def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n - 1, src, mid, dst)


hanoi(3, "A", "C", "B")
print(count)
