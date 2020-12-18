"""
观察者模式，核心抽象对象管理所有依赖他的其他类，并在设计中使其在发生变动时，主动通知并更新其他类；也叫模型-视图模式、源-收听者模式、从属者模式。
该模式必须包含两个角色：观察者和被观察对象。在刚才的例子中，业务数据是被观察对象，用户界面是观察者。观察者和被观察者之间存在“观察”的逻辑关联，当被观察者发生改变的时候，观察者就会观察到这样的变化，并且做出相应的响应。
使用场景：
一个抽象模型有两个方面，其中一个方面依赖于另一个方面。将这些方面封装在独立的对象中使它们可以各自独立地改变和复用。
一个对象的改变将导致其他一个或多个对象也发生改变，而不知道具体有多少对象将发生改变，可以降低对象之间的耦合度。
一个对象必须通知其他对象，而并不知道这些对象是谁。
需要在系统中创建一个触发链，A对象的行为将影响B对象，B对象的行为将影响C对象……，可以使用观察者模式创建一种链式触发机制。
"""


class Observer:
    def __init__(self):
        self._number = None
        self._department = []

    # 其中实现检测值的核心方法是通过property将方法伪装成属性，封装了内部的逻辑处理，而这逻辑中就包含更新相关对象的方法。
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value
        print(f'当前客户数：{self._number}')
        for obj in self._department:
            obj.change(value)
        print('--------------')

    def notice(self, department):
        # 相关部门类
        self._department.append(department)


class Hr:
    """人事部门类"""
    def change(self, value):
        if value < 10:
            print('人事变动：裁员')
        elif value > 20:
            print('人事变动：扩增')
        else:
            print('人事不受影响')


class Factory:
    def change(self, value):
        if value < 15:
            print('生产计划变动：减产')
        elif value > 25:
            print('生产计划变动：增产')
        else:
            print('生产计划维系')


if __name__ == '__main__':
    observer = Observer()
    hr = Hr()
    factory = Factory()
    observer.notice(hr)
    observer.notice(factory)
    observer.number = 10
    observer.number = 15
    observer.number = 20
    observer.number = 25
