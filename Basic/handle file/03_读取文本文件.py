with open(r"b.txt", "r", encoding="utf-8") as f:
    str1 = f.read(3)
    print(str1)

with open("b.txt", "r", encoding="utf-8") as f:
    for a in f:
        print(a)
