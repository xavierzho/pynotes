"""
组合模式：将对象组合成树状结构，来表示业务逻辑上的[部分-整体]层次，这种组合使单个对象和组合对象的使用方法一样。
优势：组合模式使得用户对单个对象和组合对象的使用具有一致性。
"""


class ComponentBases:
    """部门抽象出来的基类"""

    def __init__(self, name):
        self.name = name

    def add(self, obj):
        pass

    def remove(self, obj):
        pass

    def display(self, number=1):
        pass


class Node(ComponentBases):

    def __init__(self, name, duty):
        super(Node, self).__init__(name=name)
        # self.name = name
        self.duty = duty
        self.children = []

    def add(self, obj):
        self.children.append(obj)

    def remove(self, obj):
        self.children.remove(obj)

    def display(self, number=1):
        print(f'部门：{self.name}|级别：{number}|职责：{self.duty}')
        n = number + 1
        for obj in self.children:
            obj.display(n)


if __name__ == '__main__':
    root = Node('总经理办公室', '总负责人')
    node1 = Node('财务部', '公司财务')
    root.add(node1)
    node2 = Node('业务部', '销售产品')
    root.add(node2)
    node3 = Node('生产部', '生产产品')
    root.add(node3)
    node4 = Node('销售事业一部', 'A产品销售')
    node2.add(node4)
    node5 = Node('销售事业二部', 'B产品销售')
    node2.add(node5)
    root.display()
