# 属性：类属性和实例属性
# 类属性：就是类对象所拥有的属性，它被所有类对象的实例对象共有，类独享和实例对象可以访问
# 实例属性：实例对象所拥有的属性，只能通过实例对象访问


class Student:
    name = 'zxq'  # 属于类属性

    def __init__(self, age):
        self.age = age  # 实例属性
        pass
    pass


Student.name = '李易峰'  # 通过类对象才能去去修改类属性的数据

zxq = Student(22)  # 创建实例对象
print(zxq.name)  # 通过实例对象去访问类属性
# zxq.name = '刘德华'  # 通过实例对象，对类属性进行修改是不可以的
print(zxq.name)
print(zxq.age)



print('____________通过类对象访问name________________')
# print(Student.name)  # 如类名.属性名 形式去访问
# print(Student.age)  # age 属于实例对象所有

# 小结：类属性是可以被类对象和实例对象共同访问的
# 实例属性只能由实例对象所访问

xh = Student(20)
print('小花的数据：————————————————————————————————')
print(xh.name)
print(xh.age)
