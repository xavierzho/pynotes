class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen


class CPU:
    def calculate(self):
        print("算你个1231231")
        print("cpu对象:", self)


class Screen:
    def show(self):
        print("显示一个好看的画面,亮瞎你的钛合金眼")
        print("screen对象:", self)


m = MobilePhone(CPU(), Screen())
print(MobilePhone.__mro__)
m.cpu.calculate()

m.screen.show()
