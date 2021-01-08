"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/6
"""
from queue import Queue
import single_thread
import time
import random
from threading import current_thread, Thread


def do_craw(url_queue: Queue, html_queue: Queue):
    while True:
        url = url_queue.get()
        html = single_thread.craw(url)
        html_queue.put(html)
        print(f"{current_thread()} craw {url} | url_queue.size={url_queue.qsize()}")
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: Queue, file):
    while True:
        html = html_queue.get()
        results = single_thread.parse(html)
        for res in results:
            file.write(str(res) + '\n')
        print(f"{current_thread()} results.size={len(results)} | url_queue.size={html_queue.qsize()}")

        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = Queue()
    html_queue = Queue()
    for url in single_thread.urls:
        url_queue.put(url)
    for idx in range(3):
        t = Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw {idx}")
        t.start()
        if url_queue.empty() and html_queue.empty():
            t.join()
    file = open('producer_consumer.txt', 'w')
    for idx in range(3):
        t = Thread(target=do_parse, args=(html_queue, file), name=f"parse {idx}")
        t.start()
        if url_queue.empty() and html_queue.empty():
            t.join()



