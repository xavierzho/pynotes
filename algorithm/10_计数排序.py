import random


def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for idx, val in enumerate(count):
        for i in range(val):
            li.append(idx)


lis = [random.randint(0, 100) for _ in range(1000)]
print(lis)
count_sort(lis)
print(lis)
