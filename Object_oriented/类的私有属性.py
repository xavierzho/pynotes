class Employee:

    __company = "zxqp"  # 私有类属性

    def __init__(self, name, age):
        self.name = name
        self.__age = age    # 私有属性

    def __work(self):   # 私有方法
        print("好好工作,天天向上!")
        print("年龄:{0}".format(self.__age))
        print(Employee.__company)


e = Employee("zxq", 22)

print(e.name)
# print(e.__age)
print(e._Employee__age)
print(dir(e))
e._Employee__work()
print(e._Employee__work)