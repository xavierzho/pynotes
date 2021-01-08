"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/5
"""
import aiohttp
import asyncio
from pyquery import PyQuery as pq

headers = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,'
                         'likeGecko)Chrome/83.0.4103.116Safari/537.36'}

url = "https://www.amazon.cn/b/ref=s9_acss_bw_cg_pccateg_2a1_w?node=106200071&pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-2&pf_rd_r=PQNKPPABQXAWCTZSNFXA&pf_rd_t=101&pf_rd_p=cdcd9a0d-d7cf-4dab-80db-2b7d63266973&pf_rd_i=42689071"


async def fetch(session, url):
    async with session.get(url, headers=headers) as resp:
        suffix = resp.url.path.split('.')[-1]
        if suffix.lower() in ['jpg', 'gif', 'png', 'jpeg', 'pdf']:
            return await resp.content.read()
        else:
            return await resp.text()


async def parse_html():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session=session, url=url)
        doc = pq(html)
        h2_list = doc('h2')
        for h2 in h2_list:
            print(h2.text.strip())


async def main():
    await parse_html()


asyncio.run(main())
