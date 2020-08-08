with open("b.txt", "r", encoding="utf-8") as f:
    print("文件名是：{0}".format(f.name))
    print(f.tell())
    print("读取的内容是：{0}".format(str(f.readlines())))
    print(f.tell())
    f.seek(3)
    print("读取的内容是：{0}".format(str(f.readlines())))

