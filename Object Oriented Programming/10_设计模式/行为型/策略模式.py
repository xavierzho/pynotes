"""
策略模式，让一个类的行为或其算法可以在运行时更改，策略是让实例化对象动态的更改自身的某些方法使用的是types.MethodType绑定。

说起策略的动态更改方法，就不得不对比一下元类的动态增加方法，元类是类的抽象，它负责一个抽象类创建、实例化，是通过type函数来绑定方法。
使用场景：
1、如果在一个系统里面有许多类，它们之间的区别仅在于它们的行为，那么使用策略模式可以动态地让一个对象在许多行为中选择一种行为。
2、一个系统需要动态地在几种算法中选择一种。
3、如果一个对象有很多的行为，如果不用恰当的模式，这些行为就只好使用多重的条件选择语句来实现。
"""
import types


class People:
    def __init__(self, func=None):
        if func:
            self.speak = types.MethodType(func, self)

    def speak(self):
        print('说中文')


def speak_english(self):
    print('说英语')


def speak_german(self):
    print('说德语')


if __name__ == '__main__':
    test = People()
    test2 = People(speak_english)
    test3 = People(speak_german)
    [func.speak() for func in (test, test2, test3)]
