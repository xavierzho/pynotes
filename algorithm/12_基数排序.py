import random


def radix_sort(li):
    max_num = max(li)  # 最大值
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for val in li:
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)
        # 分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        # 写回li

        it += 1


lis = list(range(100000))
random.shuffle(lis)
radix_sort(lis)
print(lis)