import copy


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


# 赋值变量
c1 = CPU()
c2 = c1

print(c1)
print(id(c1))
print(c2)
print(id(c2))

# 浅拷贝
print("测试浅复制...")
s1 = Screen()
m1 = MobilePhone(c1, s1)
m2 = copy.copy(m1)

print(m1, m1.cpu, m1.screen)
print(m2, m2.cpu, m2.screen)

# 深拷贝
print("测试深复制...")
m3 = copy.deepcopy(m1)

print(m1, m1.cpu, m1.screen)
print(m2, m2.cpu, m2.screen)

