try:
    f = open(r"b.txt", "a", encoding="utf-8")
    str1 = ["钟锡权", "22 year old"]
    f.writelines(line + '\n' for line in str1)  # 换行推导式

except BaseException as e:
    print(e)

finally:
    f.close()

