class MyClass(object):
    def func1(self):
        print('func1')
        return self

    def func2(self):
        print('func2')
        return self


obj = MyClass()
obj.func1().func2()