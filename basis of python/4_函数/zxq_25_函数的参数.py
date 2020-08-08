def sum_2_num(num1, num2):  # 形参
    """对2个数字的求和"""

    result = num1 + num2

    print('%d + %d = %d' % (num1, num2, result))


sum_2_num(int(input('请输入第一个数字')), int(input('请输入第二个数字')))  # 实参
