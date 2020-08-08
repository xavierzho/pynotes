"""
数据类型转换
函 数	作 用
int(x)	将 x 转换成整数类型
float(x)	将 x 转换成浮点数类型
complex(real，[,imag])	创建一个复数
str(x)	将 x 转换为字符串
repr(x)	将 x 转换为表达式字符串
eval(str)	计算在字符串中的有效 Python 表达式，并返回一个对象
chr(x)	将整数 x 转换为一个字符
ord(x)	将一个字符 x 转换为它对应的整数值
hex(x)	将一个整数 x 转换为一个十六进制字符串
oct(x)	将一个整数 x 转换为一个八进制的字符串
"""

"""
姓名: 小明
年龄: 18岁
性别: 男性
身高: 1.75米
体重: 75公斤
"""

# 在 Python 中, 定义变量时是不需要指定变量的类型的
# 在运行的时候, Python 解释器,会根据赋值语句等号右侧的数据
# 自动推导出变量中保存数据的准确类型
# str表示字符串类型
name = "小明"
# int表示整数类型
age = 18
# bool 表示是一个布尔类型,真 True(非零即真) 或者 假 False
gender = False  # 不是男生
# float 表示一个浮点数(小数)类型
height = 1.75

weight = 75

print(type(name))

