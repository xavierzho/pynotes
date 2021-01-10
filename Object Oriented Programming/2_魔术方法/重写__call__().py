"""
定义了__call__方法的对象，称为“可调用对象”，
即该对象可以像函数一样被调用。
"""


# class SalaryAccount:
#     """工资计算类"""
#
#     def __call__(self, salary):
#         print("发工资啦...")
#         yearSalary = salary * 12
#         daySalary = salary // 22.5
#         hourSalary = daySalary // 8
#
#         return dict(yearSalary=yearSalary, monthSalary=salary, daySalary=daySalary, hourSalary=hourSalary)
#
#
# s = SalaryAccount()
# print(s(30000))


class A:
    def __call__(self, *args, **kwargs):
        print('执行到我了')
        self.func()

    def func(self):
        print('啦啦啦')


a = A()
a()
