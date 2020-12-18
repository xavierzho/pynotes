"""
各种类接口的合并
适配器可以理解为万能接口，各种类接口通过这个接口然后被调用，达到万能转换的效果。
实现：定义适配器类来分类，将各种类的不同方法注册到对应的函数中，调用的时候只需要使用分类名，即可达到适配所有类不同方法的效果
适配器类的三个角色：
目标抽象类：目标抽象类定义客户所需要的接口，可以是一个抽象类或接口，也可以是具体的类，在类适配器中，由于C#不支持多重继承，所以他只能是接口
适配器类：它作为一个转换器用来调用另外一个接口，对于Adapter和Target进行适配，它是适配器模式的核心
适配者类：适配者即被适配的角色，定义了一个已经存在的接口，这个接口需要适配，适配者类包好了客户希望的业务方法。
"""


class A:
    def a(self):
        print('我是A类的a方法')


class B:
    def b(self):
        print('我是B类的b方法')


class C:
    def c(self):
        print('我是C类的c方法')


class Adapter:
    """适配器类"""
    def __init__(self, classname, method):
        self.classname = classname
        self.__dict__ = method

    def __getattr__(self, item):
        return getattr(self.classname, item)


def test():
    objects = []
    AA = A()
    objects.append(Adapter(AA, dict(test=AA.a)))
    BB = B()
    objects.append(Adapter(BB, dict(test=BB.b)))
    CC = C()
    objects.append(Adapter(CC, dict(test=CC.c)))
    for obj in objects:
        obj.test()


test()
