"""
·字典通常用于存储 描述一个 物体 的相关信息
·列表和字典的区别:列表 是 有序 的对象集合;字典 是 无序 的对象集合.
·字典用 {} 定义
·字典使用 键值对 存储数据,键值对之间使用 , 分割
    ·键 key 是索引
    ·值 value 是数据
    ·键 和 值 之间用 : 分隔
    ·键必须是唯一的
    ·值 可以去任何数据类型, 但 键 只能使用 字符串 数字 或者 元组

"""

zxq_dict = {"name": '钟锡权',
            "age": 22,
            "gender": True,
            "height": 1.72,
            "weight": 60}
# 1.取值
print(zxq_dict['name'])
# 在取值的时候,如果指定的key 不存在,程序会报错

# 2.增加/修改
# 如果key 不存在,会新增键值对
zxq_dict['123'] = 30
# 如果key 存在,会修改已存在的键值对
zxq_dict['age'] = 23

# 3.删除
zxq_dict.pop('123')
# 在删除指定键值对的时候,如果指定的 key 不存在,程序会报错KeyError
# zxq_dict.pop('123333')

print(zxq_dict)

# 4.统计键值对数量
print(len(zxq_dict))

# 5.合并字典
temp_dict = {"degree": "college"}

# 注意:如果被合并的字典中包含已存在的键值对,会覆盖原有的键值对
zxq_dict.update(temp_dict)

print(zxq_dict)

# 5.清空字典
zxq_dict.clear()


print(zxq_dict)
