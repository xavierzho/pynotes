import os

print(os.name)  # windows->nt   linux->posix
print(os.sep)  # windows->\   linux->/
print(repr(os.linesep))  # windows->\r\n  linux->\n\
print(os.stat("10_os模块-文件和目录操作.py"))

# 关于工作目录的操作
print(os.getcwd())
# os.mkdir("123")  # 创建目录
# os.rmdir("123")  # 删除目录

# os.system("cmd")
os.system("ping wwww.baidu.com")
# os.system("notepad.exe")


os.startfile(r"路径")  # 调用程序
