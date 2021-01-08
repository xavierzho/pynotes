"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/7
"""
import asyncio
from functools import partial

async def get_html(url):
    print(f"start get url:{url}")
    await asyncio.sleep(2)
    print(f"end get url:{url}")
    return 'jones'


def callback(url, task):
    # partial绑定参数必须放前面
    print('parse detail', task.result(), url)


if __name__ == '__main__':
    url = 'www.baidu.com'
    loop = asyncio.get_event_loop()
    # future = asyncio.ensure_future(get_html(url))
    future = loop.create_task(get_html(url))
    future.add_done_callback(partial(callback, url))
    loop.run_until_complete(future)
    # print(future.result())
