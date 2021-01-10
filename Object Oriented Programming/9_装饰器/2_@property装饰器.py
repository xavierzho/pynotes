# 通过@property实现对私有属性的访问和修改
# setter 和getter方法


class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property  # 使用装饰器进行修饰，提供一个getter方法
    def salary(self):
        return self.__salary

    @salary.setter  # 使用装饰器进行装饰，提供一个setter方法
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("录入错误!薪水在1000--50000范围内")


"""
    def get_salary(self):
        print("salary run...")
        return self.__salary
    def set_salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("录入错误!薪水在1000--50000范围内")
"""

emp1 = Employee("zxq", 30000)
# emp1.salary()
# print(emp1.get_salary())
# emp1.set_salary(2000)
# print(emp1.get_salary())


print(emp1.salary)
emp1.salary = 2000
print(emp1.salary)
