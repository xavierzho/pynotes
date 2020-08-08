
empNum = 0
salarySum = 0
salarys = []
for i in range(4):
    s = input("请输入员工的薪资（按Q或q结束）")

    if s.upper() == "Q":
        print("录入完成，退出")
        break
    if float(s) < 0:
        continue

    salarys.append(float(s))
    salarySum += float(s)
else:
    print("数据录入全部4名员工的薪资")

print("录入薪资：", salarys)
print("平均薪资{0}".format(salarySum/4))
