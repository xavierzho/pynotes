class Person:
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age  # 实例属性

    def say_age(self):  # 实例方法
        print(self.name, "的年龄是:", self.age)


obj = object()
print(dir(obj))

s2 = Person("钟锡权", 20)
print(dir(s2))
# object 不包含实例方法和实例属性
