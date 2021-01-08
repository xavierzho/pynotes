"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/6
"""
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor() as pool:
    results = pool.map(craw, urls)
    for result in results:
        print(result)

with ThreadPoolExecutor as pool:
    futures = [pool.submit(craw, url) for url in urls]
    for future in futures:
        print(future.result())
    for future in as_completed(results):
        print(future.result())
