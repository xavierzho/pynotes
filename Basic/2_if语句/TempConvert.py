# TempConvert.py
# 评估函数  eval(<字符串或字符串变量>) 运算数字字符串函数
TempStr = input("请输入带有符号得温度值：")


if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("摄氏度是{:.2f}C".format(C))

elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("华氏度是{:.2f}F".format(F))

else:
    print("输入格式错误")
