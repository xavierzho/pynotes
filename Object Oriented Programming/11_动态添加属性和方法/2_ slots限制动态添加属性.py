# __slots__ 属性
"""
· python是动态语言，在运行的时候可以动态绑定属性，如果要限制在运行的时候给类添加属性，python允许在定义class的时候，定义一个__slots__变量，来限制该class实例能添加的属性
· 只有在__slots__变量中的属性才能被添加，没有在__slots__变量中的属性会添加失败，可以防止其他人在调用类的时候乱添加属性或方法。__slots__属性子类不会继承，只有在当前类中生效
作用：限制要添加的实例属性，可以节约内存
"""


class Student(object):
    __slots__ = ('name', 'age')

    def __str__(self):
        return '{}...{}'.format(self.name, self.age)


xw = Student()
xw.name = '小王'
xw.age = 20
# xw.score = 95  # 属性没有在限制范围内
# print(xw.__dict__)  # 所有可以用的属性都存储在这里 ,缺点就是占用内存空间大
# 通过__dict__可以看到定义了 __slots__变量之后 Student类的实例已经不能随意创建不在__slots__变量定义的属性了
# 同时也不存在__dict__这个属性了
print(xw.__str__)
print(xw)

# 假如在继承关系中使用__slots__变量
# 父类 定义的 __slots__ 变量 不会被子类继承
# 只有当子类声明了 __slots__变量，才会继承父类的__slots__变量中限制的范围+自身限制的范围的集合


class SubStudent(Student):
    __slots__ = ('gender', 'project')
    pass


ln = SubStudent()
ln.gender = '男'
ln.project = '计算机信息管理'
print(ln.gender, ln.project)
