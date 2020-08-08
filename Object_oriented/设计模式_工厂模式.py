"""
工厂模式实现了创建者和调用者的分离，使用专门的工厂类将选择实现类、创建对象进
行统一的管理和控制。
"""


class CarFactory:

    def create_car(self, brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "位置品牌,无法创建"


class Benz:
    pass


class BMW:
    pass


class BYD:
    pass


factory = CarFactory()
c1 = factory.create_car("奔驰")
c2 = factory.create_car("比亚迪")
print(c1)
print(c2)
