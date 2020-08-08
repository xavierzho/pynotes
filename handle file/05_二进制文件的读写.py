with open("E:\下载\9.19云顶装备合成.jpg", "rb") as f:
    with open("9.19云顶装备合成.jpg", "wb") as w:
        for line in f.readlines():
            w.write(line)
print("图片拷贝完成！")
