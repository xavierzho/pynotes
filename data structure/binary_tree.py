from collections import deque


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


a = BinaryTreeNode('A')
b = BinaryTreeNode('B')
c = BinaryTreeNode('C')
d = BinaryTreeNode('D')
e = BinaryTreeNode('E')
f = BinaryTreeNode('F')
g = BinaryTreeNode('G')
e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f
root = e
# print(root.lchild.rchild.data)


def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)


def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)


def after_order(root):
    if root:
        after_order(root.lchild)
        after_order(root.rchild)
        print(root.data, end=',')


def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:  # 只要队不空进行循环
        node = queue.popleft()
        print(node.data, end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


level_order(root)
