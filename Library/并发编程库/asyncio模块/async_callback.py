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
    """

    :param url:
    :param task: task对象
    :return:
    """
    # partial绑定参数必须放前面
    print('回调绑定的参数', task.result(), url)


async def main():
    base_url = 'http://www.baidu.com/'
    task = asyncio.create_task(get_html(base_url))
    await task
    task.add_done_callback(partial(callback, base_url))


if __name__ == '__main__':
    asyncio.run(main())
