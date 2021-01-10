class Person:  # 父类

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # return "名字是:{0} 年龄:{1}".format(self.name, self.age)
        return '我是str'

    def __repr__(self):
        return "名字是:{0} 年龄:{1}".format(self.name, self.age)


p = Person('zxq', 20)
print(p)

p1 = Person('123', 30)
print(p1)

r = repr(p1)
print(r)
