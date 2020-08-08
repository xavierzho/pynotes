try:
    f = open("d:/a.txt", 'r')
    content = f.readline()
    print(content)

except BaseException as e:
    print(e)

finally:
    print("我是finally中的语句，无论发生异常与否，都执行！")
    try:
        f.close()
    except BaseException as e:
        print(e)

print("程序结束")
