# 单例模式，是一种常用的软件设计模式，目的：确保一个类只有一个实例存在
# 如果希望在整个系统中，某个类只能出现一个实例的时候，那么这个单例对象就满足要求


# 创建一个单例对象，基于__new__去实现的【最推荐的一种】
print('—————————————第一种方法———————————————')


class MySingLenTon:

    __obj = None    # 类属性
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        if MySingLenTon.__init_flag:
            print("init...")
            self.name = name
            MySingLenTon.__init_flag = False


a = MySingLenTon("aa")
print(id(a))
b = MySingLenTon("bb")
print(id(b))
c = MySingLenTon("cc")
print(id(c))

print('—————————————第二种方法———————————————')


class DatabaseClass(object):
    def __new__(cls, *args, **kwargs):
        # 调用父类的__new__()
        if not hasattr(cls, '_instance'):  # 如果不存在就开始创建
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


class DBSingle(DatabaseClass):
    pass


db1 = DBSingle()
print(id(db1))
db2 = DBSingle()
print(id(db2))
db3 = DBSingle()
print(id(db3))
