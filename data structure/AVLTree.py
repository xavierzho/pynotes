from bst import BST


class AVLTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None
        self.bf = 0


class AVLTree(BST):
    def __init__(self, li: list = None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c
        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c

        p.fc = 0
        p.fc = 0
        return c

    def rotate_right_left(self, p, c):
        g = c.lchild
        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c.parent
        c.parent = g
        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        c.parent = g

        # 更新bf
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:
            # 插入的实际上是g
            g.bf = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.rchild
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c

        g.lchild = c
        c.parent = g
        s3 = g.rchild
        """
                    p
                g       s4
            c       s3    
        s1  s2       
        """
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g
        # 更新bf
        if g.bf < 0:
            # 说明插入到s2上了
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            # 说明插入到s3上了
            p.bf = 0
            c.bf = -1
        else:
            # 插入的是g
            g.bf = 0
        return g

    def insert_not_rec(self, val):
        # 1.插入到
        p = self.root
        if not p:  # 处理空树的情况
            self.root = AVLTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = AVLTreeNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # 存储插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLTreeNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:  # val == p.data
                return
        # 更新bf
        while node.parent:  # node.parent不为空
            if node.parent.lchild == node:  # 传递是从左子树来的，左子树更沉
                # 更新node.parent的bf -= 1
                if node.parent.bf < 0:  # 原来node.parent.bf == -1,更新后变成-2
                    g = node.parent.parent  # 为了链接旋转之后的子树
                    x = node.parent  # 旋转前的子树的根
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                elif node.parent.bf > 0:  # 原来node.parent.bf == 1 更新后变成0
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf == 0 更新后变成-1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:  # 传递从右子树来的，右子树更沉
                # 更新node.parent的bf += 1
                if node.parent.bf > 0:  # 原来node.parent.bf == 1 更新后变成2
                    g = node.parent.parent
                    x = node.parent  # 旋转前的子树的根
                    # 看node那边沉
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                elif node.parent.bf < 0:  # 原来node.parent.bf == -1 更新后变成0
                    node.parent.bf = 0
                    break

                else:  # 原来node.parent.bf == 0 更新后变成1
                    node.parent.bf = 1
                    node = node.parent
                    continue
            # 链接旋转后的子树
            n.parent = g
            if g:  # 如果g不为空
                if x == g.lchild:
                    g.lchild = n
                elif x == g.rchild:
                    g.rchild = n
                break
            else:
                self.root = n
                break


lis = [9, 8, 7, 6, 5, 4, 3, 2, 1]
tree = AVLTree(lis)
tree.pre_order(tree.root)
print('')
tree.insert_not_rec(tree.root)
