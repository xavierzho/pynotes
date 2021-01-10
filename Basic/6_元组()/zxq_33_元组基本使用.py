info_tuple = ('zhangsan', 18, 1.75, 'zhangsan')


# 1.取值和取索引
print(info_tuple[0])
# 已经知道的数据中，希望知道该数据在元组中的索引
print(info_tuple.index(18))

# 2.统计计数
print(info_tuple.count('zhangsan'))
# 希望统计元组中包含元素的个数
print(len(info_tuple))
