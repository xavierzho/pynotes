"""
给定一个整数数组 nums和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:

    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
"""
import time


# 第一种解法
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for x in range(n):
            for y in range(x + 1, n):
                if nums[x] + nums[y] == target:
                    return x, y
                else:
                    continue


Solution().twoSum([15, 7, 11, 2], 9)


# 第二种解法
class Solution2:
    def two_sum(self, num_list, target):
        lens = len(num_list)
        for i in range(lens):
            a = target - num_list[i]
            if a in num_list:
                y = num_list.index(a)
                if i == y:
                    continue
                else:
                    return i, y
            else:
                continue


Solution2().two_sum([15, 7, 11, 2], 9)


# 用字典提升速度
class Solution3:
    def num_sum(self, nums_list, target):
        dic = {}
        # enumerate()枚举函数：将列表中的值转化成带索引值的元组
        for idx, num in enumerate(nums_list):
            if target - num in dic:
                print(dic[target - num], idx)
                return dic[target - num], idx
            else:
                dic[num] = idx


Solution3().num_sum([15, 7, 11, 2], 9)

