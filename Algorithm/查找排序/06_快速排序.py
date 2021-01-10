from cal_time import cal_time
import random
import sys

sys.setrecursionlimit(100000)


def partition(lis, left, right):
    tmp = lis[left]
    while left < right:
        while left < right and lis[right] >= tmp:  # 从右边找比tmp小的数
            right -= 1  # 往左走一步

        lis[left] = lis[right]  # 把右边的值写到左边空位上
        # print(li)
        while left < right and lis[left] <= tmp:
            left += 1  # 往右走一步
        lis[right] = lis[left]  # 把左边的值写到右边空位上
        # print(li)
    lis[right] = tmp
    return left


# 快速排序的框架
def _quick_sort(lis, left, right):
    if left < right:  # 至少两个元素
        mid = partition(lis, left, right)
        _quick_sort(lis, left, mid - 1)
        _quick_sort(lis, mid + 1, right)


@cal_time
def quick_sort(lis):
    _quick_sort(lis, 0, len(li) - 1)


li = list(range(10000, 0, -1))
random.shuffle(li)
quick_sort(li)

print(li)
