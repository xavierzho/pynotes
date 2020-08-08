import requests
import time
import os
from multiprocessing import Process, Queue


class DownloadProcess(Process):
    def __init__(self, urls, queue):
        Process.__init__(self)
        self.urls = urls
        self.queue = queue

    # 重写父类的run方法
    def run(self):
        for image_url in self.urls:
            filename = os.path.split(image_url)[1]
            response = requests.get(image_url)
            image_data = response.content
            self.queue.put(image_data)
            self.queue.get()
            print('下载{}完毕:'.format(filename))
        self.queue.close()


if __name__ == '__main__':
    q1 = Queue(2)
    images = [
        'https://bkimg.cdn.bcebos.com/pic/d058ccbf6c81800a4768ff01bb3533fa828b472b?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UxMTY=,xp_5,yp_5',
        'https://bkimg.cdn.bcebos.com/pic/35a85edf8db1cb131b8d4a1cd754564e93584bdc?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UxMTY=,xp_5,yp_5',
        'https://bkimg.cdn.bcebos.com/pic/9d82d158ccbf6c81ddd35ae7b63eb13532fa40dc?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UxMTY=,xp_5,yp_5',
        'https://bkimg.cdn.bcebos.com/pic/80cb39dbb6fd52665f904a1ba118972bd4073601?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UxMTY=,xp_5,yp_5',
        'https://bkimg.cdn.bcebos.com/pic/e850352ac65c10383f331056b8119313b17e89d1?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2U4MA==,xp_5,yp_5'
    ]
    dlprocess = DownloadProcess(images, q1)
    dlprocess.start()

    for i in range(5):
        if dlprocess.is_alive():
            print('进程是活跃的：', i)
        else:
            print('进程结束了')
            dlprocess.close()
            break
        time.sleep(0.5)
