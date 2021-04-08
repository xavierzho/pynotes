# class TextItem:
#     def __init__(self, name):
#         self.name = name
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#
#     def __getattr__(self, item):
#         return '非字符串，不合法'
#
#
# a = TextItem('jones')
# print(a.name)
# a.age = 22
# print(a.__dict__)
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __setitem__(self, key, value):
#         setattr(self, key, value)
#
#
# p = Person('jones')
#
# p['name'] = 10
# print(p.name)


class MyDict(dict):
    def __setattr__(self, key, value):
        print('对象加.赋值，会付触发')
        self[key] = value

    def __getattr__(self, item):
        print('对象加.取值，会触发')
        return self[item]


my_dict = MyDict(name='jones', age=22)

print(my_dict['name'])
print(my_dict.name)  # 会报错，需要重写__getitem__
my_dict.name = 22

