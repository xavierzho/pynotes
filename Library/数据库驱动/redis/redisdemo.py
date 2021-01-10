import redis
# 链接数据库
client = redis.StrictRedis(host='127.0.0.1', port=6379)

# 2.设置key
key = 'ippool'

# 3.string 增加
# result = client.set(key, '1')

# 删 1 成功 0失败
# for i in key:
#     result = client.delete(i)

# 改
# result = client.set(key, '2')

# 查
result = client.smembers('temp_kuai_formal')
# result = client.keys()
print(result)
