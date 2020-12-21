import random


def sift(li, low, high):
    i = low  # 当前节点
    j = 2 * i + 1  # 左孩子
    tmp = li[low]  # 吧堆顶存储起来
    while j <= high:  # 只要j节点没有越界一直循环
        if j + 1 <= high and li[j + 1] < li[j]:  # 如果有右孩子并且比较大
            j = j + 1  # j指向的就是右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:  # tmp > li[j],将tmp放到i的位置
            break
    li[i] = tmp  # 最后都得放回叶子节点


def top_k(li, k):
    heap = li[0:k]
    for i in range(k // 2 - 1, -1, -1):
        sift(heap, i, k - 1)
    # 建堆
    for j in range(k, len(li)):
        if li[j] > heap[0]:
            heap[0] = li[j]
            sift(heap, 0, k - 1)
    # 遍历
    for x in range(k - 1, -1, -1):
        heap[0], heap[x] = heap[x], heap[0]
        sift(heap, 0, x - 1)
    # 输出结果
    return heap


lis = list(range(1000))
random.shuffle(lis)
print(top_k(lis, 10))
