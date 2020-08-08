import time
# # 基础版本
# scale = 10
# print("-----执行开始-----")
# for i in range(scale+1):
#     a = '*'*i
#     b = '·'*(scale-i)
#     c = (i/scale)*100
#     print("{:^3.0f}%[{}->{}]".format(c, a, b))
#     time.sleep(0.1)
# print("-----执行结束-----")

# # 单行刷新功能
# for f in range(101):
#     print("\r{:1}%".format(f), end="")
#     time.sleep(0.1)

scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*'*i
    b = '·'*(scale-i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:2.2f}s".format(c, a, b, dur), end="")
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2, "-"))


