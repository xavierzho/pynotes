"""
梅森旋转算法
基本随机数函数：
1.seed(a=None)
# 初始化给定的随机数种子，默认当前系统时间
random.seed(10)  产生种子10对应的序列

2.random()
# 生成一个[0.0,1.0]之间的随机小数
random.random()  0.5714925946899135

拓展随机数函数：
1.randint()
# 生成一个[a,b]之间的整数
random.randint(10,100)   64

2.randrange(m,n[,k])
# 生成一个[m,n]之间以k为步长的随机数
random.randrange(10,100,10)   80

3.getrandbits(k)
# 生成一个k比特长的随机整数
random.getrandbits(16) 37885

4.uniform(a,b)
# 生成一个[a,b]之间的随机小数
random.uniform(10,100) 13.096321648808136

5.choice(sep)
# 从序列sep中随机选择一个元素
random.choice([1,2,3,4,5,6,7,8,9])  8

6.shuffle(sep)
# 从序列sep中随机排列，返回打乱后的序列
random.shuffle([1,2,3,4,5,6,7,8,9])  [3,1,6,2,7,4,8,9,5]

"""
# 公式法
# pi = 0
# N = 100
# for k in range(N):
#     pi += 1 / pow(16, k) * ( \
#                 4 / (8 * k + 1) - 2 / (8 * k + 4) - \
#                 1 / (8 * k + 5) - 1 / (8 * k + 6))
# print("圆周率的值是：{}".format(pi))

from random import random
from time import perf_counter

# 蒙特卡罗法
DARTS = 1000 * 1000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS + 1):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits / DARTS)
print("圆周率值是：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter() - start))
