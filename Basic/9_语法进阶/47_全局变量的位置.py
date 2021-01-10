"""python代码结构
shebang
import 模块
全局变量
函数定义
执行代码
"""

# 注意：在开发时，应该把模块中额所有全局变量
# 定义在所有函数的上方，就可以保证所有函数
# 都能够正常使用

num = 10
# 再定义一个全局变量
title = "zxq"

# 在定义一个全局变量
name = "小明"


def demo():
    print("%d" % num)
    print("%s" % title)
    print("%s" % name)


demo()

