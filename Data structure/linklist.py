class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def head_linklist(li):
    # 头插法
    # 创建头
    head = Node(li[0])
    for element in li[1:]:
        # 创建节点
        node = Node(element)
        # 将头赋值给下一个节点
        node.next = head
        # 将新节点变成头
        head = node
    return head


def tail_linklist(li):
    # 创建头和尾，刚开始的时候头和尾是同一个元素
    head = Node(li[0])
    tail = head
    for ele in li[1:]:
        # 创建新节点
        node = Node(ele)
        # 新节点作为下一个节点
        tail.next = node
        # 将尾指向新节点
        tail = node
    return head


def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


lk = tail_linklist([1, 2, 3, 7, 76, 8])
print_linklist(lk)
