"""
代理模式：为其他对象提供一种代理以控制对这个对象的访问。在某些情况下，一个对象不适合或者不能直接引用另一个对象，而代理对象可以在客户端和目标对象之间起到中介作用。
组成：
抽象角色：通过接口或抽象对象声明真实对象实现的业务方法
代理对象：实现抽象角色，是真实角色的代理，通过真实角色的业务逻辑方法来实现抽象方法，并附加自己的操作
真实角色：实现抽象角色，定义真实角色所需实现的业务逻辑，供代理角色调用。
应用场景：

远程（Remote）代理：为一个位于不同的地址空间的对象提供一个局域代表对象。这个不同的地址空间可以是在本机器中，也可是在另一台机器中。远程代理又叫做大使（Ambassador）。好处是系统可以将网络的细节隐藏起来，使得客户端不必考虑网络的存在。
虚拟（Virtual）代理（图片延迟加载的例子）：根据需要创建一个资源消耗较大的对象，使得此对象只在需要时才会被真正创建。使用虚拟代理模式的好处就是代理对象可以在必要的时候才将被代理的对象加载；代理可以对加载的过程加以必要的优化。当一个模块的加载十分耗费资源的情况下，虚拟代理的好处就非常明显。
保护代理（Protection Proxy ）控制对原始对象的访问。保护代理用于对象应该有不同 的访问权限的时候
智能引用（Smart Reference）代理：当一个对象被引用时，提供一些额外的操作，比如将对此对象调用的次数记录下来等
"""


class Jurisdiction:
    def level1(self):
        print('权限等级1')

    def level2(self):
        print('权限等级2')

    def level3(self):
        print('权限等级3')

    def level4(self):
        print('权限等级4')


class Proxy:
    def __init__(self, name):
        self.user = name
        self._jurisdiction = Jurisdiction()

    def level(self):
        if self.user == 'a':
            return self._jurisdiction.level1()
        elif self.user == 'b':
            return self._jurisdiction.level2()
        elif self.user == 'c':
            return self._jurisdiction.level3()
        elif self.user == 'd':
            return self._jurisdiction.level4()
        else:
            print('无权限')


if __name__ == '__main__':
    t = Proxy('a')
    t.level()
    t.user = 'b'
    t.level()
    t.user = 'c'
    t.level()
    t.user = 'd'
    t.level()
    t.user = 'e'
    t.level()
