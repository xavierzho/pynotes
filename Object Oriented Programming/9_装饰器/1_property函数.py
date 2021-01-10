# 通过property函数实现访问私有函数
class Person(object):
    def __init__(self):
        self.__age = 20

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age

    # 定义一个类属性 实现通过直接访问属性的形式去访问私有的属性
    age = property(get_age, set_age)


p1 = Person()
print(p1.age)
p1.age = -1
print(p1.age)
# p1.get_age()
# p1.set_age()
