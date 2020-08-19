# 所谓的重写父类，就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖父类中同名的方法


class GrandFather:
    def eat(self):
        print('吃饭')

    pass


class Father(GrandFather):
    def eat(self):  # 因为父类中已经存在eat(),相当于覆盖了父类的eat()
        print('爸爸经常吃海鲜')
    pass


class Son(Father):
    pass


son = Son()
print(Son.__mro__)
son.eat()
