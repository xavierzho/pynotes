# 只能推导小数点后15位
from math import pi
b_list = [str(round(pi, i)) for i in range(1, 16)]
print(b_list)
