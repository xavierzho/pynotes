import os.path
import time

# 判断，绝对路径，是否目录，是否文件，文件是否存在
j = os.path.isabs("b.txt")
print("判断path所对应是否为绝对路径，返回True或False:{}".format(j))

i = os.path.isdir("b.txt")
print("判断path所对应是否为已存在的目录，返回True或False:{}".format(i))

h = os.path.isfile("../../../Basic/handle file/b.txt")
print("判断path所对应是否为已存在的文件，返回True或False:{}".format(h))

g = os.path.exists("../../../Basic/handle file/b.txt")
print("判断path对应文件或目录是否存在，返回True或False:{}".format(g))

# 获取文件基本信息
k = os.path.getsize("../../../Basic/handle file/b.txt")
print("返回path对应文件的大小:{}k".format(k))

a = os.path.abspath("../../../Basic/handle file/b.txt")
print("返回path在当前路径中的绝对路径:{}".format(a))

b = os.path.normpath("/handle file/b.txt")
print("归一化path的表示形式，统一用\\分隔路径:{}".format(b))

c = os.path.relpath("/handle file/b.txt")
print("返回但钱程序与文件之间的相对路径：{}".format(c))

d = os.path.dirname("c:/b.txt")
print("返回path中的目录名称：{}".format(d))

e = os.path.basename("b.txt")
print("返回path中最后的文件名称：{}".format(e))

f = os.path.join("d:/", "b.txt")
print("组合path与paths，返回一个路径字符串:{}".format(f))

l = time.ctime(os.path.getctime("../../../Basic/handle file/b.txt"))
print("返回path对应文件或目录上一次访问的时间:{}".format(l))

m = time.ctime(os.path.getatime("../../../Basic/handle file/b.txt"))
print("返回path对应文件或目录最近一次修改的时间:{}".format(m))

n = time.ctime(os.path.getmtime("../../../Basic/handle file/b.txt"))
print("返回path对应文件或目录的创建时间:{}".format(n))

# 对路径的操作
path = os.path.abspath("../../../Basic/handle file/b.txt")
print(os.path.split(path))
print(os.path.splitdrive(path))

