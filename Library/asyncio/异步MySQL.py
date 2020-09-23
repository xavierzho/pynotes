import aiomysql
import asyncio


async def execute(address, password):
    print('开始执行', address)
    # 网络IO操作：创建mysql链接
    conn = await aiomysql.connect(host=address, port=3306, user='root', password=password, db='yst_populations')

    # 网络IO操作：创建cursor对象
    cur = await conn.cursor()

    # 网络IO操作：
    await cur.execute('select * From populations')
    result = await cur.fetchall()
    print(result)
    # 网络Io操作：关闭mysql链接
    conn.close()

    await cur.close()


task_list = [execute('localhost', "1997"),
             execute('localhost', "1997")]
# asyncio.run(asyncio.wait(task_list))

# 单数据链接的
asyncio.run(execute('localhost', "1997"))
