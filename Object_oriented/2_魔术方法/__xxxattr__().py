
class A:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        # 当对象空间中没有属性的时,才执行,防止报错
        return '没有当前值'

    def __setattr__(self, key, value):
        # 实际上self.name = name 时调用__setattr__()
        print('设置值的时候执行我!')
        self.__dict__[key] = value

    def __delattr__(self, item):
        print('删除值的时候执行我')
        self.__dict__.pop(item)


a = A('jones')

print(a.name)
a.age = 19
print(a.__dict__)
del a.name
print(a.__dict__)