"""
输入：matrix = [
[1,4,7,11,15],
[2,5,8,12,19],
[3,6,9,16,22],
[10,13,14,17,24],
[18,21,23,26,30]
], target = 5
输出：true
"""

lis = [[1, 4, 7, 11, 15],
       [2, 5, 8, 12, 19],
       [3, 6, 9, 16, 22],
       [10, 13, 14, 17, 24],
       [18, 21, 23, 26, 30]]


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        h = len(matrix)
        if h == 0:
            return False
        w = len(matrix[0])
        if w == 0:
            return False
        left = 0
        right = w * h - 1
        while left <= right:  # 候选区有值
            mid = (left + right) // 2
            i = mid // w
            j = mid % w
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return False


print(Solution().searchMatrix(lis, 5))
