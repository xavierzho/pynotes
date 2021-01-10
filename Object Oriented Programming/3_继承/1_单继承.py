
# 将多个类共有的方法提取到父类中，子类仅需要继承父类即可
# 目的是提升开发效率


class Animal:
    def eat(self):
        print('吃饭了')

    def drink(self):
        pass


class Dog(Animal):
    def wwj(self):
        print('小狗汪汪叫')
    pass


class Cat(Animal):
    def mmj(self):
        print('小猫喵喵叫')
    pass


d1 = Dog()
d1.eat()  # 继承了父类的方法

print('以下猫的行为')

c1 = Cat()
c1.eat()
# NameError: name 'eat' is not defined，原因是Cat类没有这个方法
c1.drink()
