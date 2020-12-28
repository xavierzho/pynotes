class Node:
    def __init__(self, item):
        self.item = item
        self.pre = None
        self.next = None


class CreateDoubleLinkedList(object):
    """创建一个创建双向链表的类"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断双向链表是否为空链表"""
        return self.head is None

    def length(self):
        """获取双向链表的长度"""
        cur = self.head
        count = 0
        while cur is not None:

            cur = cur.next
            count += 1
        return count

    def traversal(self):
        """遍历双向链表"""
        cur = self.head
        if self.is_empty():
            print("链表为空！")
            return
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def node_is_exist(self, data):
        """查找指定结点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False

    def tail_insert(self, data):
        # 创建节点
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            tail = self.head
            # 指针移动到尾部
            while tail.next:
                tail = tail.next
            # 尾节点的向后指向新节点
            tail.next = node
            # 新节点的向前指向尾节点
            node.pre = tail

    def head_insert(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node

        else:
            # 将新节点向后指向头节点
            node.next = self.head
            # 头节点向前指向新节点
            node.pre = node
            # 头节点的
            self.head = node

    def insert_node(self, data, index):
        """在指定位置添加节点"""
        # 判断索引的位置
        if index < 0 or index > self.length():
            print('节点位置错误！')
            return False
        elif index == 0:
            self.head_insert(data)
        elif index == self.length():
            self.tail_insert(data)
        else:
            #
            node = Node(data)
            cur = self.head  # 当前节点
            pres = None
            count = 0
            # 移动到要添加的位置
            while count < index:
                pres = cur
                cur = cur.next
                count += 1
            # 新节点和它前面的节点互指
            pres.next = node
            node.pre = pres
            # 新节点和它后面的节点互指
            node.next = cur
            cur.pre = node

