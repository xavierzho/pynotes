"""
类方法：
类对象所拥有的方法，需要用装饰器@classmethod来标识其为类方法，
对于类方法，第一个参数必须是对象，
一般用cls作为第一参数，类方法可以通过类对象，实例对象调用

    定义格式：
    @classmethod
    def 类方法名(cls, 参数)：
        pass
    使用：
        类名.方法名()
        也可以通过:
        对象.方法名()
"""


class Person(object):
    country = 'china'

    @classmethod
    def get_country(cls):
        return cls.country  # 访问类属性

    @classmethod
    def change_country(cls, data):
        cls.country = data  # 修改类属性的值，在类方法中
    pass


print(Person.get_country())  # 通过类对象直接引用
p = Person()  # 创建实例对象
print('实例对象访问 %s' % p.get_country())
print('修改后的数据——————————————————————————')
Person.change_country('英国')
print(Person.get_country())