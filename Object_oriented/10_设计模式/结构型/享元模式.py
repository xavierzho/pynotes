"""
元：可理解为python中元类、最小粒度的类，系统中存在大量的相似对象时，可以选择享元模式提高资源利用率
两个状态：
内蕴状态存储在享元内部，不会随环境的改变而有所不同，是可以共享的。
外蕴状态是不可以共享的，它随环境的改变而改变的，因此外蕴状态是由客户端来保持（因为环境的变化是由客户端引起的）。

使用场景:
如果一个应用程序使用了大量的对象，而这些对象造成了很大的存储开销的时候就可以考虑是否可以使用享元模式。
例如,如果发现某个对象的生成了大量细粒度的实例，并且这些实例除了几个参数外基本是相同的，如果把那些共享参数移到类外面，在方法调用时将他们传递进来，就可以通过共享大幅度单个实例的数目。
"""


class FlyweightBase:
    def offer(self):
        """享元基类"""
        pass


class Flyweight:
    """共享享元类"""

    def __init__(self, name):
        self.name = name

    def get_price(self, price):
        print(f'产品类型：{self.name}|详情：{price}')


class FactoryFlyweight:
    """享元工厂类"""
    def __init__(self):
        self.product = {}

    def get_product(self, key):
        if not self.product.get(key, None):
            self.product[key] = Flyweight(key)
        return self.product[key]


if __name__ == '__main__':
    t = FactoryFlyweight()
    A = t.get_product('高端')
    A.get_price('香水: 80')
    B = t.get_product('高端')
    B.get_price('面膜: 800')
