"""
@Author: Jonescyna@gmail.com
@Created: 2020/12/23
"""

import random

p = 53
q = 59
n = p * q
euler = (p - 1) * (q - 1)

e = 3

d = 2011

# 加密过程
data = random.randint(0, 10000)
print(data)
c = (data ** e) % n
print(c)

# 解密过程
m = (c ** d) % n
print(m)
print(f'解密完成,数据是：{m}')
