# a = ["is sd aa", "钟锡权\n", "sde w\n"]
# b = enumerate(a)
# print(a)
# print(list(b))

with open(r"b.txt", "r", encoding="utf_8") as f:
    lines = f.readlines()
    lines = [str(index) + " " + temp.rstrip() + "\n" for index, temp in enumerate(lines)]

with open("b.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

