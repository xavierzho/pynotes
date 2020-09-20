class BMI:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    # 目的是吧bmi方法伪装成一个属性
    @property
    def bmi(self):
        return self.weight / (self.height ** 2)

    @bmi.setter
    def bmi(self, value):
        print(value)
        print('修改的时候执行我')

    @bmi.deleter
    def bmi(self):
        print('删除的时候执行我')


p = BMI('zxq', 1.72, 60)
# p.name = 'jonescy'
#
# print(p.name)
# p.bmi = 20
del p.bmi
print(p.bmi)
# 通过属性的方式查看
