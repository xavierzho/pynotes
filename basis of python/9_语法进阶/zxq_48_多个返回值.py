def measure():
    """测量温度和湿度"""

    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 元组 - 可以包含多个数据，因此可以使用元组让函数一次返回多个返回值

    return temp, wetness


result = measure()
print(result)

# 需要单独的处理温度或者湿度
print(result[0])
print(result[1])

# 如果函数返回的类型时元组，同时希望单独的处理元组中的元素
# 可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个函数接收结果时，变量的个数赢和元组中的元素的个数保持一致

gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)