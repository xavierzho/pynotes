"""
类方法：
    定义格式：
    @classmethod
    def 类方法名(cls, 参数)：
        pass
    使用：
        类名.方法名()
        也可以通过:
        对象.方法名()

静态方法：
    定义格式：
    @classmethod
    def 方法名():
        pass
    使用：
        类名.方法名()

魔术方法:
    定义格式：


"""


# 类方法操作类属性
class Student:
    # 类属性
    company = "zxq"

    # 更直接访问类方法
    @classmethod  # 静态方法（装饰器）
    def print_company(cls):  # cls是类对象本身
        print('公司名称：', cls.company)


Student.print_company()


# 定义与“类对象”无关的方法，称为“静态方法”。
class Student2:
    company = "zxq"

    @classmethod
    def add(cls, a, b):
        print("{0}+{1}={2}".format(a, b, a+b))


Student2.add(10, 20)
