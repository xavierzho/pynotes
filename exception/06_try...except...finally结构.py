try:
    a = input("请输入一个被整除数：")
    b = input("请输入一个除数：")
    c = float(a)/float(b)
    print(c)

except BaseException as e:
    print(e)

else:  # 没有异常执行的结果
    print("除以的结果：", c)

finally:
    print("我是finally中的语句，无论发生异常与否，都执行！")

print("程序结束！")
