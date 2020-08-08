class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name, "的年龄是:", self.age)


obj = object()
print(dir(obj))

s2 = Person("钟锡权", 20)
print(dir(s2))
