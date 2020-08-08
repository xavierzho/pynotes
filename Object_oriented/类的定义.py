class Student:  # 类名首字母大写，多个单词采用驼峰原则

    company = "CMRH"    # 类属性
    count = 0   # 类属性

    def __init__(self, name, score):  # 构造函数
        self.name = name  # 实例属性
        self.score = score

    def say_score(self):    # 实例方法
        print("我的公司是：", Student.company)
        print("{0}的分数是：{1}".format(self.name, self.score))


s1 = Student("钟锡权", 90)  # 通过类名来调用构造函数
# s1是实例对象，自动调用__init__()方法
s1.say_score()
print("一共创建{0}Student 对象".format(Student.count))

s1.age = 22
s1.salary = 3000

print(s1.salary)

s2 = Student("zxq", 100)
s2.say_score()

Student.say_score(s2)  # 解释器调用方法，没有本质区别

print(dir(s2))  # 查看对象所有的属性

print(s2.__dict__)


class Man:
    pass


print(type(Man))
print(id(Man))

Stu2 = Man
s3 = Stu2()
print(s3)
