
class A:
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):

        print('获取属性的时候执行我', item)
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print('添加属性的时候执行我')
        self.__dict__[key] = value
        print(key, value)

    def __delitem__(self, key):
        print('删除属性的时候执行我')
        self.__dict__.pop(key)


a = A('jones')
a['age'] = 10
print(a['name'])
print(a.__dict__)
del a['age']
print(a.__dict__)
# print(a.name)
