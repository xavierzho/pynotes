# 子类可以继承多个父类，子类同时拥有所有父类的属性和方法


class ShengXian:
    def fly(self):
        print('神仙都会飞')

    pass


class Monkey:
    def chi_tao(self):
        print("猴子喜欢吃桃")

    pass


class SunWuKong(ShengXian, Monkey):
    pass


swk = SunWuKong()
swk.fly()
swk.chi_tao()


# 问题来了，如果有同名方法呢？
# 当多个父类存在相同的方法的时候 因该去调用哪一个呢？
class D(object):
    def eat(self):
        print('D.eat')


# C中的eat()覆盖掉D中的eat()
class C(D):
    def eat(self):
        print('C.eat')
        pass

    pass


class B(D):
    pass


class A(B, C):
    pass


a = A()
a.eat()
print(A.__mro__)  # 打印类的继承关系
# 在执行eat()时，查找方法的顺序是：
# 先到B中查找，在到第二个父类C中查找，如果C类中没，则到D类中查找
# 否则将会报错 A->B->C->D

