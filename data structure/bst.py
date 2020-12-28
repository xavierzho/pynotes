import random


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None


class BST:
    def __init__(self, li: list = None):
        self.root = None
        if li:
            for val in li:
                self.insert_not_rec(val)

    def insert(self, node, val):
        if not node:
            node = BinaryTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node

        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node

        return node

    def insert_not_rec(self, val):
        p = self.root
        if not p:  # 处理空树的情况
            self.root = BinaryTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    # 左孩子不存在
                    p.lchild = BinaryTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BinaryTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def pre_order(self, root):
        """前序遍历"""
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        """中序遍历"""
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    def after_order(self, root):
        """后序遍历"""
        if root:
            self.after_order(root.lchild)
            self.after_order(root.rchild)
            print(root.data, end=',')

    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif val < node.data:
            return self.query(node.lchild, val)
        else:
            return node

    def query_not_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def __remove(self, node):
        """node是叶子节点"""
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
            node.parent = None
        else:
            node.parent.rchild = None
            node.parent = None

    def __remove_lchild(self, node):
        # 删除的是左孩子
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.rchild.parent = node.parent

    def __remove_rchild(self, node):
        # 删除的是右孩子
        if not node.parent:
            self.root = node.rchild

        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent

        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:
            node = self.query_not_rec(val)
            if not node:
                return False
            if not node.lchild and node.rchild:
                self.__remove(node)
            elif not node.rchild:
                # 只有一个左孩子的情况
                self.__remove_lchild(node)
            elif not node.lchild:
                # 只有一个右孩子的情况
                self.__remove_rchild(node)
            else:
                # 两个孩子节点都存在
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除min_node
                if min_node.rchild:
                    self.__remove_rchild(min_node)
                else:
                    self.__remove(min_node)


# lis = [1, 4, 2, 5, 3, 8, 6, 9, 7]
#
# tree = BST(lis)
# tree.in_order(tree.root)
# print('')
# tree.delete(4)
# tree.delete(8)
# print('')
# tree.in_order(tree.root)
