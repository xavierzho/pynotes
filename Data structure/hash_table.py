# 用拉链法写一个哈希表

class LinkList:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    class LinkListIterator:
        """迭代器类"""

        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable: list = None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def remove(self, k):

        ...

    def __iter__(self):
        # 迭代器
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return '>>' + ",".join(map(str, self)) + ">>"


class HashTable:
    """类似于集合的结构"""
    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for _ in range(self.size)]

    def h(self, k):
        return k % self.size

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print('Duplicated insert.')
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)

    def remove(self, k):
        i = self.h(k)
        self.T[i].remove(k)


ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(20)
ht.insert(102)
ht.insert(508)
# print(ht.find(101))
ht.remove(102)
print(ht.T)
