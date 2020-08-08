# 浅拷贝
import copy

a = [10, 20, [6, 9]]
b = copy.copy(a)

print("a:", a)
print("b:", b)

b.append(30)
b[2].append(7)

print("拷贝到。。。")

print("a:", a)
print("b:", b)

print("#" * 50)
"""深拷贝"""


def testDeepCopy():
    a1 = [10, 20, [6, 9]]
    b1 = copy.deepcopy(a1)

    print("a1:", a1)
    print("b1:", b1)

    b1.append(30)
    b1[2].append(7)

    print("拷贝到。。。")

    print("a1:", a1)
    print("b1:", b1)


testDeepCopy()

print("#" * 50)
# 传递不可变对象时，不可变对象包含的子对象是可变的，是浅拷贝
c = (19, 20, [5, 6])
print("c:", id(c))


def test01(m):
    print("m:", id(m))
    m[2][0] = 888
    print(m)
    print("m:", id(m))


test01(c)
print(c)
