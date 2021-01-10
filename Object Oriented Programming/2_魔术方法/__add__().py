class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        print('执行加法的时候触发我')
        return self.a + other.a


a = A(10)
b = A(20)
print(a + b)

