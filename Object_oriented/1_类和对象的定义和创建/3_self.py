# self和对象指向同一个内存地址，
class Man:
    def __init__(self, pro):
        # self标识符，表示实例对象本身
        self.pro = pro

    def eat(self, name, food):
        # print('self=%s' % id(self))
        print('%s 喜欢吃 %s，修的专业是%s' % (name, food, self.pro))
        pass
    pass


# xm是一个新的实例化对象
xm = Man('HRM')
# print('xm=%s' % id(xm))
xm.eat('张三', '鸡翅')

# self就是实例化对象的本身
# xm=1775569369224
# self=1775569369224

# self只有在类中定义 实例方法的时候才有意义，在调用的时候不必传入响应的参数，而解释器会自动取指向

