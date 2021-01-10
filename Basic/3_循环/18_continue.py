i = 0

while i < 10:
    if i == 3:

        # continue 结束本次循环，继续下一次循环
        # 在使用关键字之前，需要确认循环的计数是否修改
        # 否者可能会导致死循环
        i += 1

        continue

    print(i)

    i += 1


