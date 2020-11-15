import time

# 结构化时间->时间戳
s_time = time.localtime()
print(time.mktime(s_time))

# 时间戳->结构化时间
tp_time = time.time()
# 东八区的时间
print(time.localtime(tp_time))
# 世界标准时间
print(time.gmtime())

# 结构化时间->格式化字符串形式时间
print(time.strftime('%Y-%m-%d %H:%M:%S', s_time))

# 格式化时间字符串->结构化时间
str_time = "2020-08-11 23:28:09"
# 先转化为结构化时间
timeArray = time.strptime(str_time, '%Y-%m-%d %H:%M:%S')
print(timeArray)
# 再转化为时间戳

