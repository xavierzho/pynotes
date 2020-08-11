import time

print(time.time())  # 获取当前的时间戳
print(time.ctime())  # 易懂的方式获取时间
print(time.gmtime())  # 生成一个程序可以立用的时间格式

print("=" * 50)

"""
strftime(tpl,ts)
# tpl是格式化模板字符串，用来定义输出效果
  ts 是计算机内部时间类型变量
"""
t = time.gmtime()
# print(time.strftime("%Y-%m-%d %B-%b %H-%I:%M:%S %p", t))
# print("=" * 50)

# timeStr = time.strftime("%Y-%m-%d  %H:%M:%S", t)
# print(time.strptime(timeStr, "%Y-%m-%d  %H:%M:%S"))

"""
perf_counter()
# 返回一个CPU级别的精确时间计数值，单位为秒；由于这个计数值棋典不确定，连续调用差值猜有意义
"""
# start = time.perf_counter()
# end = time.perf_counter()
# print(end - start)

"""
sleep(s)
# s拟休眠的时间，单位为秒，可以是浮点数
"""


# def wait():
#     time.sleep(3.3)
#
#
# wait()  # 程序将停滞3.3秒后


# 字符串类型的时间
str_time = "2020-08-11 23:28:09"
# 先转化为数组
timeArray = time.strptime(str_time, '%Y-%m-%d %H:%M:%S')
# 在转化为时间戳
end_time_stamp = int(time.mktime(timeArray))
now = int(time.time())
print(end_time_stamp)
print(now)
if now > end_time_stamp:
    print('该ip地址过期了')
else:
    print('还没过期')
