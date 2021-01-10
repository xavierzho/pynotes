"""
try:
    被监控的可能发生异常的语句块
except BaseExcetion[as e]：
    异常处理语句块

"""
print("step0")
try:
    print("step1")
    a = 3/0
    print("step2")  # 跳过异常处理

except BaseException as e:
    print("step3")
    print(e)

print("step4")

