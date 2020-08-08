# 析构对象
class Person:

    def __del__(self):
        print("销毁对象:{0}".format(self))


p1 = Person()
p2 = Person()

del p2
print("程序结束")

# 程序结束也会调用__del__()方法

