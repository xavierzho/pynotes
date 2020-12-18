"""
定义一个算法或者流程，部分环节设计为外部可变，用类似于模板的思想来实例化一个实体，可以往模板中填充不同的内容；在模板思想下，实体的整体框架是确定的，他是一个模板，但是模板下内容可变，从而实现了动态的更新流程或算法。
看了模板方法后，感觉和之前的一个设计模式比较相似《建造者模式》，但是建造者模式是将对象的构建和表示分离，相同的构建生成不同的表示对象，而模板方法是将定义的算法或流程中的部分环节推迟到子类中实现算法或流程的可变，这是二者本质的区别。
"""


class User:
    def __init__(self, name, shop, times, number):
        self.name = name
        self.shop = shop
        self.times = times
        self.number = number


class Handle:
    def __init__(self, user=None):
        self.user = user

    def invoicen(self):
        string = """打印小票
        客户：{}
        商品：{}
        数量：{}
        时间：{}
        """.format(self.user.name, self.user.shop, self.user.number, self.user.times)
        print(string)

    def make(self):
        print(f'制作完成：{self.user.shop} 数量：{self.user.number}')

    def run(self):
        self.invoicen()
        self.make()


if __name__ == '__main__':
    test = Handle()
    xiaoming = User('小明', '汉堡', '17：50', '5')
    test.user = xiaoming
    test.run()
