#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import csv
import json


def get_data():
    urls = ['https://dncapi.bqiapp.com/api/coin/web-coinrank?page={page}&type=-1&pagesize=100&webp=1'.format(page=item)
            for item in range(1, 65)]
    headers = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,'
                             'likeGecko)Chrome/83.0.4103.116Safari/537.36'}
    url_list = []
    for url in urls:
        print(url)
        r = requests.get(url, headers=headers)
        data = json.loads(r.content.decode())

        for item in data['data']:
            name = item['name']
            full_name = item['fullname']
            code = item['code']
            final_url = 'https://www.feixiaohao.com/currencies/{}/'.format(item['code'])
            url_list.append([code, final_url, full_name, name])
    return url_list


def download(data):
    fp = open('Library/asyncio/FeiXiaHao_mapping_data.csv', 'a', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(['code', 'item_url', 'full_name', 'name'])
    for i in data:
        writer.writerow(i)


download(get_data())
