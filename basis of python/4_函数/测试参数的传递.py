# 传递可变对象

a = [10, 20]

print(id(a))
print(a)
print('*' * 50)


def test01(m):
    print(id(m))
    m.append(300)
    print(id(m))


test01(a)
print(a)

print("#" * 50)

# 传递不可变对象(产生新的对象)


b = 100


def test02(n):
    print("n:", id(n))
    n += 200
    print("n:", id(n))
    print(n)


test02(b)
print("b:", id(b))

