# 为了更好的保存属性的安全，即不能随意修改，将属性定义为私有属性，添加一个可调用的方法去访问，不让子类去继承
# 私有属性的语法：__age = 18 声明该属性为私有，不能在类的外部被使用或直接访问


class Person:
    __hobby = '跳舞'

    def __init__(self):
        self.__name = '李四'  # 实例属性私有化
        self.age = 20

    def __str__(self):
        return '{}的年龄是{},爱好是{}'.format(self.__name, self.age, self.__hobby)  # 私有化属性在内部可以访问的

    def change_value(self):
        Person.__hobby = '唱歌'


class Student(Person):
    def print_info(self):
        # print(self.__name)  # 在此访问父类中的私有属性，是不行的
        print(self.age)
    pass


# x1 = Person()
# # print(x1.__name)  # 通过类对象的外部是不能访问的
# print(x1)
stu = Student()
stu.change_value()

print(stu)
# print(stu.__name)  # 不能被子类继承
stu.print_info()

# print(stu.__hobby)  # 实例对象不能访问私有类属性
# print(Person.__hobby)  # 类对象不能访问私有类属性

# 小结：
# 1.私有化的实例属性，不能在外部直接访问，可以在类的内部随意使用
# 2.子类不能继承父类的私有化属性【只能继承公共的属性和方法】
# 3.__属性 直接变成私有化属性

