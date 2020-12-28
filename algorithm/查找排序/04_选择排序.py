def select_sort_simple(lis):
    lis_new = []
    for i in range(len(lis)):
        min_val = min(lis)
        lis_new.append(min_val)
        lis.remove(min_val)
    return lis_new


def select_sort(lis):
    for i in range(len(lis) - 1):  # i表示第几趟
        min_loc = i
        for j in range(i + 1, len(lis)):
            if lis[j] < lis[min_loc]:
                min_loc = j
        if min_loc != i:
            lis[i], lis[min_loc] = lis[min_loc], lis[i]
        print(lis)


li = [3, 24, 6, 2, 2, 4, 6, 21]
print(li)
print(select_sort(li))
