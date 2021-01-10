import types  # 添加方法库


def dymicmethod(self):
    print('{} 的体重是:{} kg,在 {} 读大学'.format(self.name, self.weight, Student.school))

@classmethod
def class_test(cls):
    print('这是个类方法')

@staticmethod
def static_method_test():
    print('这是个静态方法')


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{}今年{}岁了'.format(self.name, self.age)


print('榜单类方法')
Student.TestMethod = class_test
Student.TestMethod()

print('------------------绑定类方法结束--------------------')
Student.TestStaticMethod = static_method_test
Student.TestStaticMethod()
print('------------------绑定静态方法结束--------------------')


zxq = Student('钟锡权', 23)
zxq.weight = 60  # 动态添加的实例属性
zxq.print_info = types.MethodType(dymicmethod, zxq)  # 动态绑定方法
# print(zxq)
# print(zxq.weight)
zxq.TestMethod()
print('zxq实例对象调用动态绑定类方法')
print('------------------另外一个实例对象 张明--------------------')
zm = Student('张明', 22)
print(zm)
# print(zm.weight)
print('------------------给类对象添加属性--------------------')
Student.school = '北京邮电大学'  # 动态添加类属性
# print(zm.school)
zm.weight = 90
zm.print_info = types.MethodType(dymicmethod, zm)
print('------------------执行动态调用实例方法--------------------')
zxq.print_info()  # 调用动态绑定的方法
zm.print_info()

