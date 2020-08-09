import aiomysql
import asyncio


async def execute(address, password):
    print('开始执行', address)
    # 网络IO操作：创建mysql链接
    conn = await aiomysql.connect(host='127.0.0.1', port=3306, user='root', password='1997')

    # 网络IO操作：创建cursor对象
    cur = await conn.cusor()

    # 网络IO操作：
    await cur.execute('select host,User From user')

    # 网络Io操作：关闭mysql链接
    conn.close()

    await cur.closed()
    print('结束', address)

task_list = [execute('redis://localhost:6379', ''),
             execute('redis://localhost:6379', '')]

asyncio.run(asyncio.wait(task_list))
