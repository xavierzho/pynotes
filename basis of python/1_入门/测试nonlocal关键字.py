# nonlocal声明外层局部变量
# global声明全局变量

a = 100


def outer():
    b = 10

    def inner():
        nonlocal b
        print("inner b:", b)
        b = 20
        global a
        a = 10000

    inner()
    print("outer b:", b)


outer()
print("a:", a)


