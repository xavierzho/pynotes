# break 结束整个循环

while True:
    a = input("请输入一个字符（请暑促Q或者q时候退出）：")
    if a == "q" or a == "Q":
        print("循环结束，退出")
        break
    else:
        print(a)

# continue 结束本次循环，继续下一次循环

empNum = 0
salarySum = 0
salarys = []
while True:
    s = input("请输入员工的薪资（按Q或q结束）")

    if s.upper() == "Q":
        print("录入完成，退出")
        break
    if float(s) < 0:
        continue
    empNum += 1
    salarys.append(float(s))
    salarySum += float(s)

print("员工数{0}".format(empNum))
print("录入薪资：", salarys)
print("平均薪资{0}".format(salarySum/empNum))






