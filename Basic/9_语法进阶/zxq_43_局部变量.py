def demo1():

    # 定义一个局部变量
    # 1> 出生：执行了下方的代码之后才会被创建
    # 2> 死亡：函数执行结束
    num = 10

    print(num)

    num = 20

    print("在demo1函数内部的变脸是 %d " % num)

# print("%d" % num)


def demo2():

    # print("%d" % num)
    pass


demo1()
demo2()

print("over")