def outer():
    print("outer running....")

    def inter01():
        print("inter running....")

    inter01()  # 嵌套函数（内部函数），在哪里产生在哪里调用


outer()

print('#' * 50)

"""
def printChineseName():
    print("{0} {1}".format(famllyName, name))


def printEnglishName():
    print("{0} {1}".format(name, famllyName))
"""
# 避免代码重用


def printName(isChinese, name, famllyName):
    def inner_print(a, b):
        print("{0} {1}".format(a, b))

    if isChinese:
        inner_print(famllyName, name)
    else:
        inner_print(name, famllyName)


printName(True, "锡权", "钟")
printName(False, "Zhong", "Tins Qua")
