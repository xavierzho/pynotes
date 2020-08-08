"""
python中一切皆为对象
Python 中，一切皆对象。每个对象由：标识{内存地址}（identity）、类型（type）、value（值）
组成。

变量位于：栈内存。
对象位于：堆内存。

"""
a = 3
print(id(3))
# 1616609456
print(type(3))
# <class 'int'>
# a的id = 3的id
