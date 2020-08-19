"""
在子类中，如果想要获得父类的方法时，我们可以通过 super()来做。
 super()代表父类的定义，不是父类对象。
 """


class A:
    def say(self):
        print("A", self)


class B(A):

    def say(self):
        # A.say(self)
        super().say()
        print('B', self)


B().say()
