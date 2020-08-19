# 创建返回一个实例对象，调用了一次，就会得到一个对象
"""
注意事项：
· __new__是在一个对象实例化的时候所调用的第一个方法
· __new__至少必须要有一个参数cls，表示实例化的类，此参数在实例化时由python解释器自动提供的，其他的参数是用来直接传递给__init__()
· __new__绝地是否要使用该__init__(),因为__new__可以调用其他类的构造方法或直接返回别的实例对象来作为本类的实例，如果__new__没有返回实例对象，则__init__()不会被调用
· 在__new__()中，不能调用自己的__new__()，即：return cls.__new__(cls),否则会报错（RecursionError: maximum recursion depth exceeded while calling a Python object:超过最大递归深度）
"""


class Person:  # 父类

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('__init__()执行：')

    # 实际上是静态方法
    # 在python中，如果不重写__new__()默认结构如下
    def __new__(cls, *args, **kwargs):  # 也是实例方法
        """
        打印对象 自定义对象 改变输出的内容格式
        场景：控制创建对象的一些属性限定，经常用来做单例模式的时候来做
        :return
        """
        print('__new__()的执行：')
        return super().__new__(cls)  # 在这真正的创建实例对象
        # return object.__new__(cls)  # 同上的第二种写法


p = Person('zxq', 20)  # 实例化的过程会自动调用__new__()去创建实例
print(p)
# 第一个执行的是__new__()创建对象，然后返回给__init__()
# __new__()和__init__()的区别
# __new__()是类的实例化方法，必须返回该实例，否则对象创建不成功
# __init__()用来做数据属性初始化工作的，也可以认为是实例的构造方法接受类的实例，通过self并对其进行构造
# __new__(cls) 至少一个参数是cls代表实例化的类，此参数在实例化的时候，由python解释器自动提供

