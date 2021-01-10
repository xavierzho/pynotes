"""
#### 堆排序的过程

1.  简历堆
2.  得到堆顶元素，为最大元素
3.  去掉堆顶，将堆最后一个元素放到堆顶
4.  堆顶元素为第二大元素
5.  重复步骤3，直到堆变空
"""
import heapq


def sift(li, low, high):
    """
    向下调整函数
    :param li: 列表
    :param low: 堆顶
    :param high:堆的最后一个元素
    :return:
    """
    i = low  # 当前节点
    j = 2 * i + 1  # 左孩子
    tmp = li[low]  # 吧堆顶存储起来
    while high >= j:  # 只要j节点没有越界一直循环
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果有右孩子并且比较大
            j = j + 1  # j指向的就是右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:  # tmp > li[j],将tmp放到i的位置
            break
    li[i] = tmp  # 最后都得放回叶子节点


def heap_sort(li):
    n = len(li)
    for i in range(n//2 - 1, -1, -1):
        # i 建堆的时候调整部分的根的下标
        sift(li, i, n - 1)
    # 堆键完成
    for j in range(n - 1, -1, -1):
        # j指向当前堆的最后一个叶子节点
        li[0], li[j] = li[j], li[0]
        sift(li, 0, j - 1)  # j-1永远是堆的最后一个


if __name__ == '__main__':
    lis = list(range(100))
    import random

    random.shuffle(lis)
    print(lis)
    # 手写
    # heap_sort(lis)
    # 内置方法

    heapq.heapify(lis)  # 建立堆
    n = len(lis)
    for i in range(n):
        print(heapq.heappop(lis), end=',')  # 弹出最小的元素
    # print(lis)



