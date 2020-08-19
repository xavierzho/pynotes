"""

大白话：
类：是一组相同或相似特征【属性】和行为【方法】的一系列【多个】对象组合
对象：是实实在在的一个东西，类的实例化，具象化

类是对象的抽象化，而对象是类的一个实例
"""


class Student:  # 类名首字母大写，多个单词采用大驼峰原则

    company = "CMRH"    # 类属性
    count = 0   # 类属性

    def __init__(self, name, score):  # 构造函数
        self.name = name  # 实例属性
        self.score = score

    def say_score(self):    # 实例方法
        print("我的公司是：", Student.company)
        print("{0}的分数是：{1}".format(self.name, self.score))


s1 = Student("钟锡权", 90)  # 创建实例对象（类的实例化）
# s1是实例对象，自动调用__init__()方法
s1.say_score()
print("一共创建{}Student 对象".format(Student.count))

s1.age = 22
s1.salary = 3000

print(s1.salary)

s2 = Student("zxq", 100)  # 创建实例对象（类的实例化）
s2.say_score()

Student.say_score(s2)  # 解释器调用方法，没有本质区别

print('对象所有的属性:{}'.format(dir(s2)))  # 查看对象所有的属性

print(s2.__dict__)

