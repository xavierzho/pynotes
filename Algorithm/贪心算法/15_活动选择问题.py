"""
@Author: Jonescyna@gmail.com
@Created: 2020/12/22
"""
# 贪心的是最早结束时间
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
# 保证活动按照结束时间排序
activities.sort(key=lambda x: x[1])


def activity_selection(a):
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:  # 当前活动的开始时间小于等于最后一个入选活动的结束时间
            res.append(a[i])

    return res


print(activity_selection(activities))