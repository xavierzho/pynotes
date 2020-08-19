# 对象在程序运行结束后进行对象销毁的的时候调用这个方法，来释放资源
# 析构对象



class Person:
    def __init__(self, name):
        self.name = name
        print('__init__方法被调用')

    def __del__(self):
        print("销毁对象:{0}".format(self))


p1 = Person('zxq')
p2 = Person('123')

del p2  # 手动清理删除对象
print("程序结束")

# 程序结束也会调用__del__()方法
