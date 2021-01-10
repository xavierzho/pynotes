def insert_sort(li):
    for i in range(1, len(li) - 1):  # i表示拿到的派的下标
        tmp = li[i]
        j = i - 1  # j表示的手里的排
        while li[j] > tmp and j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        print(li)


li = [3, 2, 4, 1, 5, 7, 9, 6, 8]
print(li)
insert_sort(li)
