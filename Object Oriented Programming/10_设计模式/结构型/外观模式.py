"""
外观模式：也成为‘过程模式’，为子系统中的一组接口提供一个一致的解码，Facade模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。
与适配器模式不同的是，外观模式是为了统一接口，规范接口的使用；而适配器模式是为了合并接口，使接口更好的调用
在以下情况下可以考虑使用外观模式：
(1)设计初期阶段，应该有意识的将不同层分离，层与层之间建立外观模式。
(2) 开发阶段，子系统越来越复杂，增加外观模式提供一个简单的调用接口。
(3) 维护一个大型遗留系统的时候，可能这个系统已经非常难以维护和扩展，但又包含非常重要的功能，为其开发一个外观类，以便新系统与其交互。
优点
（1）实现了子系统与客户端之间的松耦合关系。
（2）客户端屏蔽了子系统组件，减少了客户端所需处理的对象数目，并使得子系统使用起来更加容易。
"""
class API1:
    def save(self):
        print('保存数据A')

    def remove(self):
        print('删除数据A')

class API2:
    def save(self):
        print('保存数据B')

    def remove(self):
        print('删除数据B')


class Facade:
    def __init__(self):
        self._api1 = API1()
        self._api2 = API2()

    def save_all(self):
        [obj.save() for obj in [self._api1, self._api2]]

    def del_all(self):
        [obj.remove() for obj in [self._api1, self._api2]]


if __name__ == '__main__':
    t = Facade()
    t.del_all()
    t.save_all()

