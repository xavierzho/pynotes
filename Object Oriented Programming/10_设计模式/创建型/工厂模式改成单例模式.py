class CarFactory:

    __obj = None  # 类属性
    __init_flag = True

    def create_car(self, brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "位置品牌,无法创建"

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, ):
        if CarFactory.__init_flag:
            print("init...")
            CarFactory.__init_flag = False


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

factory2 = CarFactory()
print(factory)
print(factory2)

