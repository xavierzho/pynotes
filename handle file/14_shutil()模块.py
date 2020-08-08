"""
shutil模块是python标准库中提供的，主要用来做文件和
文件夹的拷贝、移动、删除等；还可以做 文件和文件夹的
压缩、解压缩操作。 os模块提供了对目录或文件的一般操
作。shutil模块作为补充，提供了移动、复制、压缩、解压
等操 作，这些os模块都没有提供。
"""
import shutil
import zipfile

# shutil.copyfile("1", "1_copy.txt")

# shutil.copytree("movie/港台", "电影")  # 只能拷贝不存在的文件目录

# shutil.copytree("movie/港台", "电影", ignore=shutil.ignore_patterns("*.html", "htm"))  # ignore 忽略某些文件

shutil.make_archive("电影/gg", "zip", "movie/港台")  # make_archive（目标文件/指定文件名，压缩格式，被压缩文件）

# 压缩
# z1 = zipfile.ZipFile("aa_zip.zip", "w")
# z1.write("aa")
# z1.write("电影")
# z1.close()


# 解压
z2 = zipfile.ZipFile("aa/aa_zip.zip", "r")
z2.extractall("aa")
z2.close()

