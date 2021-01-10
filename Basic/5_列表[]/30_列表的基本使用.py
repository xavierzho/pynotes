name_list = ['zhangsan', 'lisi', 'wangwu']

# 1.取值和去索引
# list index out of range =列表索引超出范围
print(name_list[2])

# 知道数据的内容，想确定数据在列表中的位置
# 使用index方法需要注意，如果传递的数据不在列表中，程序会显示错误ValueError：is not in list = 不在列表当中
print(name_list.index('wangwu'))

# 2.修改数据
name_list[1] = '李四'
# IndexError: list assignment index out of range = 索引错误：列表指定的索引超出范围
# name_list[3] = '王小二'

# 3.增加
# append 方法可以向列表的末尾追加数据
name_list.append('王小二')
# insert 方法可以在列表的指定索引位置插入数据
name_list.insert(1, '小妹妹')

# extend 方法可以把其他列表的完整数据，添加到当前列表的末尾
temp_list = ['孙悟空', '猪八戒', '沙僧']
name_list.extend(temp_list)

# 4.删除
# remove 方法可以重列表中删除指定的数据 remove first occurrence of value = 删除第一个出现的数据
name_list.remove('wangwu')
# pop 方法默认可以把列表的最后一个元素删除
name_list.pop()
name_list.pop(3)
# clear 清除列表所有内容
# name_list.clear()

# 使用 del 关键字删除列表元素
# del 本质上事用来将一个变量从内存中删除
del name_list[2]
# 5.统计
# len(length 长度）函数可以统计列表中元素的总数
list_len = len(name_list)
print('列表中包含 %d 个元素' % list_len)

# count 方法可以统计.列表中某个数据出现的次数
count = name_list.count('zhangsan')
print('zhangsan出现了 %d 次' % count)

num_list = [6, 7, 8, 10, 1]

# 升序
name_list.sort()
num_list.sort()
print(name_list)
print(num_list)

# 降序
name_list.sort(reverse=True)
num_list.sort(reverse=True)
print(name_list)
print(num_list)

# 逆序（反转）
name_list.reverse()
num_list.reverse()
print(name_list)
print(num_list)
