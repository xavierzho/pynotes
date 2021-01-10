# 方法一
score = int(input("请输入一个在0-100之间的数字："))

if score > 100 or score < 0:
    score = int(input("输出错误！请重新输入一个在0-100之间的数字："))
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"

    else:
        grade = "E"

    print("分数为{0}，等级为{1}".format(score, grade))

# 方法二
score = int(input("请输入一个在0-100之间的数字："))
degree = "A B C D E"
num = 0
if score > 100 or score < 0:
    print("请输入一个0-100的分数")
else:
    num = score//10
    if num < 6:
        num = 5
    print("分数为{0}，等级为{1}".format(score, degree[9-num]))

