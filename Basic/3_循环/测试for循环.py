"""
for 变量 in 可迭代对象（序列，字符串，元组）
    循环体语句

"""
for x in (10, 20, 30):
    print(x)

for x1 in "sadasdgas":
    print(x1)
print("-"*50)
# 字典遍历成元组
d = {"name": "钟锡权", "age": "22", "job": "123"}
for x2 in d:
    print(x2)
for x2 in d.keys():
    print(x2)
for x2 in d.values():
    print(x2)
for x2 in d.items():
    print(x2)

print("-"*50)

sum_all = 0
sum_old = 0  # 100以内的奇数和
sum_even = 0  # 100以内的偶数和

for x3 in range(101):
    sum_all += x3
    if x3 % 2 == 1:
        sum_old += x3
    else:
        sum_even += x3

print("100以内累加总和{0}，奇数和{1}，"
      "偶数和{2}"
      .format(sum_all, sum_old, sum_even))


# 打印九九乘法表
for m in range(1, 10):
    for n in range(1, m+1):
        print("{0}*{1}={2}".format(m, n, (m*n)), end="\t")
    print()


# 用列表和字典存储信息
tb = []
r1 = dict(name="高小一", age="19", salary=30000, city="北京")
r2 = dict(name="高小二", age="20", salary=20000, city="深圳")
r3 = dict(name="高小三", age="21", salary=10000, city="上海")
tb = [r1, r2, r3]

for x in tb:
    if x.get("salary") > 15000:
        print(x)





