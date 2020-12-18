"""
简要理解：建造者，顾名思义是修建筑的建筑工人，按照基本的施工方式：打桩-浇筑框架-砌墙-装修，同样的施工流程却能建造千差万别的建筑，因为不同的设计、不同的材料，可以表现出千差万别
关键要素：相同的流程、不同的表示、修建者，也就是在同一对象在同一修建者组织下，以相同的实例化流程来表达不同的效果

"""


class Builder:
    """建造流程：原料-施工"""

    def __init__(self):
        self.materiel = None
        self.design = None

    def run(self):
        print(f'修建完工！建筑设计：{self.design}|购买原料：{self.materiel}')


class A(Builder):
    """方案A：修建毛坯房"""

    def get_materiel(self):
        self.materiel = '砖瓦'

    def get_design(self):
        self.design = '毛坯房'


class B(Builder):
    """方案B：修建毛坯房"""

    def get_materiel(self):
        self.materiel = '玻璃'

    def get_design(self):
        self.design = '写字楼'


class Director:
    """调度：买原料-组织施工"""

    def __init__(self):
        self.programme = None

    def build(self):
        self.programme.get_materiel()
        print(f'购买原料：{self.programme.materiel}')
        self.programme.get_design()
        print(f'设计方案：{self.programme.design}')
        self.programme.run()


if __name__ == '__main__':
    test = Director()
    """修建毛坯房"""
    test.programme = A()
    test.build()

    """修建写字楼"""
    test.programme = B()
    test.build()
