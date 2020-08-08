import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no': 1,
    'name': 'Nowcoder',
    'url': 'http://www.nowcoder.com'
}
# Python 字典格式 转成json对象
json_str = json.dumps(data1)
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])


# 2.文件对象 和 字典 转换
list2 = [{'num': 1, 'name': 'Nowcoder', 'url': 'http://www.nowcoder.com'},
         {'nujm': 2, "name": "zhangsan", 'url': "http://www.baidu.com"}]

str_data = json.dumps(list2)
# 把列表写入文件，该方法不用转成字符串
json.dump(list2, open('jsondemo.json', 'w'))

# 读取json文件
result = json.load(open('jsondemo.json', 'r'))
print(result)
