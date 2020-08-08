class Person:  # 父类

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "名字是:{0} 年龄:{1}".format(self.name, self.age)


p = Person('zxq', 20)
print(p)





