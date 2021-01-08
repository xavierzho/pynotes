"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/6
"""
import single_thread
from concurrent.futures import ThreadPoolExecutor, as_completed

# craw
with ThreadPoolExecutor() as pool:
    htmls = pool.map(single_thread.craw, single_thread.urls)
    htmls = list(zip(single_thread.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print('craw over')

# parse

with ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(single_thread.parse, html)
        futures[future] = url
    # for fut, url1 in futures.items():
    #     print(url1, fut.result())
    for fut in as_completed(futures):
        url = futures[fut]
        print(url, fut.result())
