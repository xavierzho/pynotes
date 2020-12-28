"""
@Author: Jonescyna@gmail.com
@Created: 2020/12/23
"""


def gcd_rec(a, b):
    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)


def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


print(gcd(12, 16))
