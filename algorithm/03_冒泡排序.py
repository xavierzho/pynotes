import random


def bubble_sort(lis):
    print(lis)
    for i in range(len(lis) - 1):  # 第i趟
        exchange = False
        for j in range(len(lis) - i - 1):
            if lis[j] < lis[j + 1]:  # 升序：第一个数比第二个数大则交换，降序：第一个数比第二个数小则交换
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                exchange = True
        print(lis)
        if not exchange:
            return


# li = [random.randint(0, 100) for i in range(10)]
li = [9, 8, 7, 6, 1, 2, 3, 4, 5]
bubble_sort(li)

