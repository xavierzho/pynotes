# 所谓的多态就是，定义时的类型和运行时的类型不一样，此时就造成为多态。
# 目的也是增加代码的可拓展性


class Animal:
    def say_who(self):
        print('我是一只动物...')

        pass

    pass


class Duck(Animal):
    def say_who(self):
        print('我是一只鸭子')
        pass

    pass


class Dog(Animal):
    def say_who(self):
        print('我是一只小狗')

    pass


class Cat(Animal):
    def say_who(self):
        print('我是一只小猫咪')

    pass


# 新增类无需调用
class Bird(Animal):
    def say_who(self):
        print('我是一只黄鹂鸟')

    pass


class People:
    def say_who(self):
        print('我是人类')
    pass


class Student(People):
    def say_who(self):
        print('我是一个一年级学生 zxq')

# duck1 = Duck()
# duck1.say_who()
#
# dog1 = Dog()
# dog1.say_who()
#
# cat1 = Cat()
# cat1.say_who()


def commonInvoke(obj):
    # 不关注类型，只关注是否有这个方法
    obj.say_who()


list_obj = [Duck(), Dog(), Cat(), Bird(), Student()]
for item in list_obj:
    commonInvoke(item)


