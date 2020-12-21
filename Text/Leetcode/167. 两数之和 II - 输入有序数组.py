
# 与1相似
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
