# 注意：定义好函数之后，只表示这个函数封装了一段代码
# 如果不主动调用函数，函数时不会主动执行的

name = "小明"


# Python解释器知道下方定义了一个函数
def say_hello():
    """打招呼"""
    print("hello 1")
    print("hello 2")
    print("hello 3")


print(name)

say_hello()

print(name)
