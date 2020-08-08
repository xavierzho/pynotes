# 列表推导式
y = [x for x in range(1, 5)]
print(y)

y1 = [x1*2 for x1 in range(1, 20) if x1 % 5 == 0]
print(y1)


cells = [(row, col) for row in range(1, 10) for col in range(1, 10)]
print(cells)

# 字典推导式
my_text = "i love you , i love stx ,w qet yq we qqo gh"
char_count = {c: my_text.count(c) for c in my_text}
print(char_count)
# 集合推导式
b = {x*2 for x in range(1, 5)}
print(b)


# 生成器推导式（生成元组）
# 一个生成器只能运行一次
gnt = (x for x in range(1, 100) if x % 9 == 0)

for x in gnt:
    print(x, end=",")


