"""
静态方法：
类对象所拥有的方法，需要用@staticmethod来表示静态方法，静态方法不需要修该参数
    定义格式：
    @staticmethod
    def 方法名():
        pass
    使用：
        类名.方法名()

魔术方法:
    定义格式：


"""


# 定义与“类对象”无关的方法，称为“静态方法”。
class Person(object):
    country = 'china'

    @classmethod
    def get_country(cls):
        return cls.country  # 访问类属性

    @classmethod
    def change_country(cls, data):
        cls.country = data  # 修改类属性的值，在类方法中

    pass

    @staticmethod
    def get_data():
        return Person.country  # 通过类对象去引用类属性

    @staticmethod
    def add(x, y):  # 带有参数的静态方法
        return x+y


print(Person.add(2, 3))

print(Person.get_data())  # 类对象来访问
people = Person()  # 创建实例对象
# print(people.get_data())  # 一般情况下，不会通过实例对象访问静态方法，这样没有意义

# 为什么要使用静态方法？
# 由于静态方法主要来存放逻辑性的代码，本身和类以及实例对象没有交互，
# 也就是说在静态方法中，不会涉及到类中方法和属性的操作
# 数据资源能够得到有效的充分利用


# demo：返回当前系统时间
import time


class TimeTest:
    def __init__(self, hour, min, second):
        self.hour = hour
        self.min = min
        self.second = second

    @staticmethod
    def show_time():
        return time.strftime('%H:%M:%S', time.localtime())


print(TimeTest.show_time())
# 没有必要通过实例对象来访问静态方法，因为参数传递没有意义
# t = TimeTest(2, 10, 15)
# print(t.show_time())
