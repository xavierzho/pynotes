"""
将其他对象之间的交互装在中介者对象中，达到松耦合、隐式引用、独立变化，与代理模式有相似之感《代理模式模式》，但是代理模式是结构性模式，侧重于对对象调用的接口控制，而中介者模式是行为性模式，解决对象与对象之间相互调用的行为问题。
使用场景：
1、系统中对象之间存在比较复杂的引用关系，导致它们之间的依赖关系结构混乱而且难以复用该对象。
2、想通过一个中间类来封装多个类中的行为，而又不想生成太多的子类。
注意事项：不应当在职责混乱的时候使用。
"""


class Consumer:
    """消费者类"""

    def __init__(self, product, price):
        self.name = '消费者'
        self.product = product
        self.price = price

    def shopping(self, name):
        # 买东西
        print(f'向{name}购买{self.price}价格内的{self.product}产品')


class Producer:
    """生产者类"""

    def __init__(self, product, price):
        self.name = '生产者'
        self.product = product
        self.price = price

    def sale(self, name):
        # 卖东西
        print(f'向{name}销售{self.price}价格的{self.product}产品')


class Mediator:
    """中介者类"""

    def __init__(self):
        self.name = '中介者'
        self.producer = None
        self.consumer = None

    def sale(self):
        # 进货
        self.consumer.shopping(self.producer.name)

    def shopping(self):
        # 出货
        self.producer.sale(self.consumer.name)

    def profit(self):
        # 利润
        print(f'中介净赚：{self.consumer.price - self.producer.price}')

    def complete(self):
        self.sale()
        self.shopping()
        self.profit()


if __name__ == '__main__':
    consumer = Consumer('手机', 3000)
    producer = Producer('手机', 2550)
    mediator = Mediator()
    mediator.consumer = consumer
    mediator.producer = producer
    mediator.complete()
