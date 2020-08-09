import aioredis
import asyncio


async def execute(address, password):
    print('开始执行', address)
    # 网络IO操作：创建redis链接
    redis = await aioredis.create_redis(address, password=password)

    # 网络IO操作：在redis中设置哈希值car，内部再设三个键值对
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    # 网络IO操作：去redis中获取值
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    # 网络Io操作：关闭redis链接
    redis.close()

    await redis.wait_closed()
    print('结束', address)

task_list = [execute('redis://localhost:6379', ''),
             execute('redis://localhost:6379', '')]

asyncio.run(asyncio.wait(task_list))
