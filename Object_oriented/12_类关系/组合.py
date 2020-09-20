
class Person:

    def __init__(self, name, hp, job, ak):
        self.name = name
        self.hp = hp
        self.job = job
        self.ak = ak

    def knife(self, obj):
        print(f'{self.name}划了一下{obj.name},{obj.name}掉了10滴血')

    def shooting(self, obj):  # obj传进来就是依赖
        self.ak.fire(self, obj)  # 封装在自己的对象的中就是组合


class Police(Person):

    call = '警察'


class Bandit(Person):

    call = '土匪'


class AK:
    def __init__(self):
        self.ak = 90

    def fire(self, obj, obj1):
        print(f'{obj.name}使用AK打了一下{obj1.name},{obj1.name}掉了90滴血')


# 1.实例化一个枪对象
ak1 = AK()
# 2. 实例化一个警察对象
p = Police('海报突击队', 100, '警察', ak1)
# 3.实例化一个土匪对象
b = Bandit('山雕', 100, '土匪', ak1)
# 警察.拿(ak, 打土匪)
# p.shooting(b)
# b.shooting(p)
p.knife(b)
b.knife(p)

# class A:
#     def __init__(self, a, b, e):
#         self.a = a
#         self.b = b
#         self.e = e
#
#     def show(self):
#         # print(id(self.e))
#         print(self.e.c, self.e.d)
#
#
# class B:
#     def __init__(self, c, d):
#         self.c = c
#         self.d = d
#
#     def index(self):
#         print('这是B类的方法')
#
#
# b1 = B(20, 30)
# print(id(b1))
# a1 = A(1, 10, b1)
# a1.show()
