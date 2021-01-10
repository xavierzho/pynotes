# 所谓的重写父类，就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖父类中同名的方法
# 为什么要重写，父类的方法已经不满足子类的需要，那么子类就可以重写父类的方法或完善父类


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def jiao(self):
        print('汪汪叫')


class KeJi(Dog):
    def __init__(self, name, color):  # 属于重写父类的方法
        # 针对这种需求，我们需要去调用父类的构造函数
        # Dog.__init__(self, name, color)  # 手动调用父类的方法 ，执行完毕就可以具备name, color 这2个实例属性了
        super().__init__(name, color)  # 自动找到父类，进而调用父类的方法，假设继承了多个父类，那么会按照顺序逐个去找，直到找到为止
        # 拓展子类其他的实例属性
        self.height = 90
        self.weight = 20

    def __str__(self):
        return '{}的颜色去{},它的身高是{}cm,体重是{}'.format(self.name, self.color, self.height, self.weight)

    def jiao(self):  # 属于重写父类的方法
        super().jiao()  # 调用父类的方法
        print('叫的跟神一样')
        print(self.name)
    pass


kj = KeJi('柯基犬', 'red')
kj.jiao()
print(kj)
