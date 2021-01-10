# 对于私有属性,继承但是不能直接使用
class Person:  # 父类

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def say_age(self):
        print("年龄,年龄,我也不知道")


class Student(Person):  # 子类

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score


print(Student.mro())

s = Student("zxq", 22, 90)

s.say_age()
print(s.name)
# print(s.age)
print(s.Person.__age)  # 间接访问父类私有属性

print(dir(s))
