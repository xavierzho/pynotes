a = 20
b = 30
c = a + b
d = a.__add__(b)
print("c=", c)
print("d=", d)

# 重写__add__()
class Person:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            return "{0}--{1}".format(self.name, other.name)
        else:
            return "不是同类对象,不能相加"

    def __mul__(self, other):
        if isinstance(other, int):
            return self.name*other
        else:
            return "不是同类对象,不能相乘"


p1 = Person("zxq")
p2 = Person("zzq")

x1 = p1 * p2
print(x1)
x2 = p1 + p2
print(x2)
