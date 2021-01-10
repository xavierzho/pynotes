def sum_2_num(num1, num2):
    """对2个数字求和"""

    result = num1 + num2

    # 可以使用返回值，告诉调用函数一方计算的结果
    return result
    # 注意： return 表示返回， 下方代码不会被执行


# 可以使用变量， 来接受函数执行的返回结果

sum_result = sum_2_num(10, 24)

print("计算结果：%d" % sum_result)
