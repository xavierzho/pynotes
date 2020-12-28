def binary_search(lis, ele):
    left = 0
    right = len(lis) - 1
    while left <= right:  # 候选区有值
        mid = (left + right) // 2
        if lis[mid] == ele:
            return mid
        elif lis[mid] > ele:  # 待查找的值的在mid左侧
            right = mid - 1
        else:  # lis[mid]<ele  待查找的值在mid右侧
            left = mid + 1
    else:
        return None


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(li, 3))
