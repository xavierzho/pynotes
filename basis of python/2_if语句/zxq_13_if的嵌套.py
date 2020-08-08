# 定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True

# 定义整型变量 knife_length 表示刀的长度,单位:厘米
knife_length = 15

# 首先检查是否有车票,如果有,允许进行安检
if has_ticket:
    print("车票检查通过，准备开始安检")
    # 如果超过20厘米,提示道具长度,不允许上车
    if knife_length > 20:
        print("您携带的道具过长，有 %d 公分长!" % knife_length)
        print("不允许上车")
    # 如果不超过20里面,安检通过
    else:
        print("安检通过，祝您旅途愉快！")


# 如果没有车票，不允许进门
else:
    print("请先购买车票再来安检！")