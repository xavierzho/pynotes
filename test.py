from urllib.parse import urljoin
nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
print(nums)


def sum_three():
    n = len(nums)

    res = []
    r = n - 1
    i = 0
    for a in range(n):
        l = i + 1
        for j in range(l, n):

            _sum = [nums[i], nums[l], nums[r]]
            if sum(_sum) < 0:
                l += 1
            elif sum(_sum) == 0:
                res.append(_sum)
            else:
                r -= 1
            # if l == r:
            #     i += 1
            #     break
    print(res)


sum_three()
