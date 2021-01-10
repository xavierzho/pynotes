import random


def merge(li, low, mid, high):
    """
    归并操作
    :param li:
    :param low:
    :param mid:
    :param high:
    :return:
    """
    i = low  # 左边列表
    j = 1 + mid  # 右边列表
    ltmp = []
    while i <= mid and j <= high:  # 只要左右都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # 其中一部分没有数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp


# li = [2, 4, 6, 7, 1, 3, 5, 8]
# merge(li, 0, 3, 7)
# print(li)

def merge_sort(li, low, high):
    """
    利用递归思想
    :param li:
    :param low:
    :param high:
    :return:
    """
    if low < high:  # 至少有2个元素
        mid = (low + high) // 2
        merge_sort(li, low, mid)  # 递归左边
        merge_sort(li, mid + 1, high)  # 递归右边
        # merge(li, low, mid, high)  # 归并
        print(li[low: high + 1])


lis = list(range(10))
random.shuffle(lis)
print(lis)
merge_sort(lis, 0, len(lis) - 1)
print(lis)
