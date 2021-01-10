"""
桥接，指的是一座桥连接两岸，而Python程序设计中的桥接指的是抽象部分和实体部分的连接，简单来说就是类和类实例化的连接。
优点：桥接模式通过类和类的实例化中间作用，使其抽象和实现可以独立变化而互不干扰
核心：通过封装，将一个抽象类的相关参数和方法分别作为桥接类的属性，这样在实例化桥接类后通过修改桥接类的属性，即可实现抽象和实现之间的独立变化。
关键词：抽象化、实现化、解耦合
抽象化：存在于多个实体中的共同的概念联系，就是抽象化，作为一个过程，抽象化是忽略一些信息，从而把不同的实体当做同样的实体对待。
实现化：抽象化给出的具体实现
解耦合：所谓的耦合，就是两个实体的行为的某种强关联。而将他们的强关联去掉，就是解耦合。在这里，解耦合指的是抽象化和实现化之间的耦合解开，或者说将它们之间的强关联改成弱关联。因此，桥接模式中的解耦合，就是指一个软件系统的抽象化和实现化之间使用组合或聚合的关系而不是继承的关系，从而使两者相对独立的变化。
"""


class A:
    def run(self, name):
        print(f'my name is :{name}')


class B:
    def run(self, name):
        print(f'我的名字是:{name}')


class Bridge:
    def __init__(self, age, classname):
        self.age = age
        self.classname = classname

    def bridge_run(self):
        self.classname.run(self.age)


if __name__ == '__main__':
    test = Bridge('jones', A())
    test.bridge_run()
    test.age = 'Tome'
    test.bridge_run()
    test.classname = B()
    test.bridge_run()
    test.age = '李华'
    test.bridge_run()
