
num = 1


def a1():
    global num  # 如果要在函数内改变全局变量，需要global声明一下
    num += 1
    print("a1")
    if num < 3:
        a1()


def b1():
    print("b1")


a1()
