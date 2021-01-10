"""
try:
    被监控的可能发生异常的语句块
except Exception1：
    处理Exception1异常处理语句块

except Exception2：
    处理Exception2异常处理语句块

...

except BaseException:
    处理BaseException异常处理语句块
"""
try:
    a = input("请输入一个被整除数：")
    b = input("请输入一个除数：")
    c = float(a)/float(b)
    print(c)

except ZeroDivisionError:
    print("异常，不能除以0")
except ValueError:
    print("异常，不能将字符串转化成数字！")
except NameError:
    print("异常，变量不存在！")
except BaseException as e:
    print(e)
