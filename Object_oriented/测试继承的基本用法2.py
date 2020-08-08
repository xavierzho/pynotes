class Person:  # 父类

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def say_age(self):
        print("年龄,年龄,我也不知道")

    def say_introduce(self):
        print("我的名字是{0}".format(self.name))


class Student(Person):  # 子类

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score

    def say_introduce(self):
        """重写父类的方法(修改父类的办法)"""
        print("我的名字是{0}".format(self.name))


s = Student("zxq", 22, 90)
s.say_age()
s.say_introduce()
