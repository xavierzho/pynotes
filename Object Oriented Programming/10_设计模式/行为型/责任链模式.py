"""
将多个处理方法连接成一条链条，请求将在这条链条上流动直到该链条中有一个节点可以处理该请求；通常这条链条是一个对象包含对另一个对象的引用而形成链条，每个节点有对请求的条件，当不满足条件将传递给下一个节点处理。\
责任链模式有几个要点：
一个对象中含有另一个对象的引用以此类推形成链条
每个对象中应该有明确的责任划分即处理请求的条件
链条的最后一节应该设计成通用请求处理，以免出现漏洞
请求应该传入链条的头部
"""


class Bases:
    def __init__(self, obj=None):
        self.obj = obj

    def screen(self, number):
        pass


class A(Bases):
    def screen(self, number):
        if 200 > number > 100:
            print(f'{number}划入A集合')
        else:
            self.obj.screen(number)


class B(Bases):
    def screen(self, number):
        if number >= 200:
            print(f'{number}划入B集合')
        else:
            self.obj.screen(number)


class C(Bases):
    def screen(self, number):
        if 100 >= number:
            print(f'{number}划入C集合')


if __name__ == '__main__':
    test = [10, 100, 150, 200, 300]
    c = C()
    b = B(c)
    a = A(b)
    for i in test:
        a.screen(i)
