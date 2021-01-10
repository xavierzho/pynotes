try:
    a = input("请输入一个被整除数：")
    b = input("请输入一个除数：")
    c = float(a)/float(b)
    print(c)

except BaseException as e:
    print(e)

else:
    print("除以的结果：", c)

print("程序结束！")
