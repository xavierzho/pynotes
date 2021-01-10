"""
@Author: Jonescyna@gmail.com
@Created: 2020/12/23
"""


class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    @staticmethod
    def gcd(a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def cm(self, a, b):
        # a = 12 b = 16 -> 4 最大公约数
        # 最小公倍数=a除以最大公约数Xb除以最大公约数*最大公约数= a/4*b/16*4=48
        x = self.gcd(a, b)
        return a * b / x

    def __str__(self):
        # return f"{self.a}/{self.b}"
        if self.b == 1:
            return '%d' % self.a
        return "%d/%d" % (self.a, self.b)

    def __add__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        if b == d:
            return Fraction(a + c, b)
        denominator = self.cm(b, d)  # 分母
        molecular = a * denominator / b + c * denominator / d  # 分子
        return Fraction(molecular, denominator)

    def __sub__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        denominator = self.cm(b, d)  # 分母
        molecular = a * denominator / b - c * denominator / d  # 分子
        return Fraction(molecular, denominator)

    def __mul__(self, other):
        molecular = self.a
        denominator = self.b
        molecular1 = other.a
        denominator2 = other.b
        return Fraction(molecular * molecular1, denominator * denominator2)

    def __truediv__(self, other):
        molecular = self.a
        denominator = self.b
        molecular1 = other.a
        denominator2 = other.b
        return Fraction(molecular * denominator2, molecular1 * denominator)

    def __pow__(self, power=2, modulo=None):
        molecular = self.a
        denominator = self.b
        return Fraction(molecular ** power, denominator ** power)


a = Fraction(1, 3)
b = Fraction(1, 2)
print(a / b)
