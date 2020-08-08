score = int(input("请输入分数："))

grade = ""
# 多分支结构存在逻辑关系，顺序是关键

if score < 60:
    grade = "不及格"
elif score < 80:
    grade = "及格"
elif score < 90:
    grade = "良好"
else:
    grade = "优秀"
print("分数是{0},等级是{1}".format(score, grade))
