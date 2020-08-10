def search1(data, x):  # 函数定义
    for i in data:
        # if i.key==x:
        if i == x:
            return i
    return -1  # 表示失败


def search2(data, x):
    for i in range(len(data)):
        if data[i] == x:
            return data[i]
    return -1


def search3(data, x):
    try:
        pass
    except ValueError:
        return -1
    p = data.index(x)
    return p


def main():  # 主函数
    data = [1, 2, 3, 4, 5]  # 函数调用
    x = int(input("input x:"))
    i1 = search1(data, x)
    i2 = search2(data, x)
    i3 = search3(data, x)
    if i1 != -1 and i2 != -1 and i3 != -1:
        print('{}is in{}'.format(x, data))
    else:
        print('{}is not in {}'.format(x, data))


if __name__ == '__main__':
    main()  # 调用main函数开始执行
