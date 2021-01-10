import csv
import json
import requests
import ssl
import random
import asyncio
import aiohttp
import re
import time
from lxml import etree
from asyncio.queues import Queue
from aiosocksy import Socks5Auth
from aiosocksy.connector import ProxyConnector, ProxyClientRequest


class Common:
    task_queue = Queue()
    result_queue = Queue()
    mark_cap_all = 0
    currency_rate = 0


# 线上的内网
socksS_address_prod = [{'http': '114.104.131.84:4526'}]
DEPLOY_MODE = 'dev'


async def session_get(session, url, socks):
    auth = Socks5Auth(login='...', password='...')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    timeout = aiohttp.ClientTimeout(total=20)
    response = await session.get(url,
                                 proxy=socks,
                                 proxy_auth=auth,
                                 headers=headers,
                                 timeout=timeout,
                                 ssl=ssl.SSLContext())
    return await response.text(), response.status


async def download(url):
    connector = ProxyConnector()
    if DEPLOY_MODE == 'dev':
        socks = None
    elif DEPLOY_MODE == 'Prod':
        socks = random.choice(socksS_address_prod)
    async with aiohttp.ClientSession(
            connector=connector,
            request_class=ProxyClientRequest
    )as session:
        ret, status = await session_get(session, url, socks)
        if 'window.location.href' in ret and len(ret) < 1000:
            url = ret.split("window.location.href='")[1].split("'")[0]
            ret, status = await session_get(session, url, socks)
            return ret, status


async def parse_html(cid, url, response):
    coin_info = {}
    coin_value = {}

    coin_info['url'] = url
    coin_info['cid'] = cid
    coin_info['time'] = int(time.time())
    tree = etree.HTML(response)

    try:
        # 美元
        price_usd = tree.xpath('//div[@class="sub"]/span[1]/span/text()')[0].strip()
        if '?' not in price_usd:
            coin_value['price'] = float(price_usd)
    except:
        pass

    try:
        # 涨跌
        updown = tree.xpath('//div[@class="sub smallfont"]/span/text()')[0].strip()
        coin_value['updown'] = float(updown)
    except:
        pass

    try:
        # 24小时成交额
        volume_24h_rmb = tree.xpath('//div[@class="chart_list"]/div[3]/div[2]/span/text()')[0].strip().replace(',', '')
        coin_value['volume_24h_rmb'] = int(float(volume_24h_rmb)) / Common.currency_rate
    except:
        pass

    try:
        # 流通量
        circulating_supply = tree.xpath('//div[@class="chart_list"]/div[2]/div[2]/text()')[0].strip().replace(',', '')
        if '?' not in circulating_supply:
            circulating_supply = re.match(r'^(\d+)(\w+)$', circulating_supply).group(1)
        coin_value['circulating_supply'] = int(circulating_supply)
    except:
        pass

    try:
        if coin_value['price'] and coin_value['circulating_supply']:
            market_cap = coin_value['price'] * coin_value['circulating_supply']
            coin_value['market_cap'] = market_cap
    except:
        pass

    try:
        if coin_value['market_cap']:
            global_share = coin_value['market_cap'] / Common.mark_cap_all
            if global_share < 0.001:
                coin_value['global_share'] = '<0.1%'
            else:
                coin_value['global_share'] = str((global_share * 100).__round__()) + '%'
    except:
        pass

    try:
        circulation_rate = tree.xpath('//div[@class="chart_list"]/div[2]/div[3]/div[2]/text()')[0].strip()
        if "?" not in circulation_rate:
            coin_value['circulating_rate'] = circulation_rate
    except:
        pass

    try:
        # 换手率
        turnover_rate = tree.xpath('//div[@class="chart_list"]/div[3]/div[2]/div[1]/div[2]/text()')[0].strip()
        if "?" not in turnover_rate:
            coin_value['turnover_rate'] = turnover_rate
    except:
        pass

    try:
        # 发行时间
        issue_time = tree.xpath('//div[@class="coinIntroduce"]/div[3]/div[1]/span[2]/text()')[0].strip()
        if issue_time != '-':
            coin_value['issue_time'] = issue_time
    except:
        pass

    try:
        # 上架交易所
        exchange_num = tree.xpath('//div[@class="coinIntroduce"]/div[3]/div[4]/span[2]/text()')[0].strip().replace('家',
                                                                                                                   '')
        coin_value['exchange_num'] = int(exchange_num)
    except:
        pass

    try:
        # 总供应量
        total_circulation = \
            re.findall('\d+,\\d+,\\d+', tree.xpath('//div[@class="coinIntroduce"]/div[3]/div[3]/span[2]/text()')[0])[
                0].replace(',', '')
        coin_value['total_circulation'] = int(total_circulation)
    except:
        pass
    coin_info['value'] = coin_value
    return coin_info


async def speed_monitor():
    while Common.task_queue.qsize() != 0:
        old_queue_len = Common.task_queue.qsize()
        await asyncio.sleep(5)
        new_queue_count = Common.task_queue.qsize()
        print('=' * 50)
        print('speed = ', (old_queue_len - new_queue_count) / 5)


async def monitor_finish():
    while len(asyncio.Task.all_tasks()) > 3:
        await asyncio.sleep(1)
    await asyncio.sleep(5)
    raise SystemExit()


async def push_results():
    temp_q = []
    while 1:
        try:
            await asyncio.sleep(3)
            for _ in range(Common.result_queue.qsize()):
                temp_q.append(await Common.result_queue.get())
            if len(temp_q) > 0:
                await push(temp_q)
                temp_q.clear()
        except:
            import traceback
            push_results(traceback.format_exc())


async def down_and_parse_task(queue):
    while 1:
        try:
            cid, url = queue.get_nowait()[:2]
        except:
            return
        for retry_cnt in range(3):
            try:
                html, status = await download(url)
                if status != 200:
                    html, status = await download(url)
                if '访问控制拒绝了你的请求' in html:
                    html, status = await download(url)
                html_parse_result = await parse_html(cid, url, html)
                print(html_parse_result)
                await Common.result_queue.put(html_parse_result)
                break
            except:
                await asyncio.sleep(0.2)
                continue


async def push(data):
    url = 'http://127.0.0.1:5000/'
    error = None
    for retry_cnt in range(3):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, data=json.dumps(data)) as response:
                    pass
                response.raise_for_status()
        except Exception as e:
            await asyncio.sleep(0.2)
            print(e)


async def get_marketcap():
    url = 'https://www.feixiaohao.com/api/home/global?webp=0'
    response = requests.get(url)
    response_json = json.loads(response.text)
    marketcap = response_json['data']['marketcapvol']
    Common.mark_cap_all = int(marketcap)


async def get_currency_rate():
    url_rate = 'https://dncapi.feixiaohao.com/api/coin/web-rate/'
    response = requests.get(url_rate)
    currency_rate = json.loads(response.text)[11]['cny']
    Common.currency_rate = currency_rate


# 程序的时间上限
async def time_limit():
    await asyncio.sleep(280)
    raise SystemExit()


async def main():
    csv_render = csv.reader(open('../../../内置模块/json or csv/FeiXiaHao_mapping_data.csv', encoding='utf-8'))
    for row in csv_render:
        try:
            if row[1].startswith('https'):
                await Common.task_queue.put(row)
        except Exception as e:
            print(e)
    print(Common.task_queue)

    await get_marketcap()
    print('总市值', Common.mark_cap_all)

    await get_currency_rate()
    print('汇率', Common.currency_rate)

    for _ in range(10):
        loop.create_task(down_and_parse_task(Common.task_queue))
    loop.create_task(monitor_finish())
    loop.create_task(speed_monitor())
    loop.create_task(push_results())
    loop.create_task(time_limit())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()  # 程序一直运行
