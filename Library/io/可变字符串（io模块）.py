import io
str01 = "hello,钟锡权"
str01io = io.StringIO(str01)

print(str01io)

str01io.getvalue()
# 需要更改字符串的索引值
str01io.seek(6)
# 更改字符串的内容
str01io.write("Z")
# 获取新的字符串
str02io = str01io.getvalue()

print(str02io)




