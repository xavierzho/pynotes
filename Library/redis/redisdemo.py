import redis

# 链接数据库
client = redis.StrictRedis(host='127.0.0.1', port=6379)

# 2.设置key
key = 'pyone'

# 3.string 增加
# result = client.set(key, '1')

# 删 1 成功 0失败
# result = client.delete(key)

# 改
# result = client.set(key, '2')

# 查
result = client.get(key)
result = client.keys()
print(result)
