import random


def insert_sort(li, gap):
    for i in range(gap, len(li) - gap):  # i表示拿到的派的下标
        tmp = li[i]
        j = i - gap  # j表示的手里的排
        while li[j] > tmp and j >= 0:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort(li, d)
        d //= 2


lis = list(range(1000))
random.shuffle(lis)
shell_sort(lis)
print(lis)
