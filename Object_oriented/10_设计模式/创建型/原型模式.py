"""
快速实例化的一种途径
原型模式相对于复制、克隆而言，但是不同于模板，模板创造出来的东西是一摸一样的，而原型创造的东西是允许差异化和个性化的存在
原型模式的核心是：拷贝（深拷贝）、属性更新（__dict__的更新）
原型模式的精要：定义一个原型，设计一个拷贝接口，不需要频繁实例化类，只需要拷贝原型对象，
优点：减少因为对象实例化而产生的小号，并实行动态装载。
"""
import copy


class Information:

    def __init__(self):
        self.name = None
        self.age = None
        self.height = None

    def run(self):
        print(f'我叫{self.name}：年龄：{self.age}，身高：{self.height}')


class Prototype:
    def __init__(self, obj):
        self.copy_obj = obj()

    def clone(self, **attrs):
        obj = copy.deepcopy(self.copy_obj)
        obj.__dict__.update(attrs)
        return obj


if __name__ == '__main__':
    test = Prototype(Information)
    a = test.clone(name='jones', age='30', height='170com')
    a.run()
    b = test.clone(name='tins', age='20', height='180cm')
    b.run()
