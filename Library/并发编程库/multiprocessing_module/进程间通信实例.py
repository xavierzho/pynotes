import requests
import time
from multiprocessing import Process, Queue


def download(urls, queue):
    for image_url in urls:
        response = requests.get(image_url)
        image_data = response.content
        queue.put(image_data)


def save_file(queue):
    count = 0
    while True:
        try:
            data = queue.get(timeout=5)  # 进程阻塞
            # 保存到本地
            fileName = 'img' + str(count) + '.jpg'
            with open('images/' + fileName, 'wb') as ws:
                ws.write(data)

            count += 1
            print('保存{}完毕！'.format(fileName))
        except Exception as err:
            print('没有更多数据了！')
            break


if __name__ == '__main__':
    q1 = Queue(2)
    images = [
        'https://bkimg.cdn.bcebos.com/pic/d058ccbf6c81800a4768ff01bb3533fa828b472b?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UxMTY=,xp_5,yp_5',
        'https://bkimg.cdn.bcebos.com/pic/35a85edf8db1cb131b8d4a1cd754564e93584bdc?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UxMTY=,xp_5,yp_5',
        'https://bkimg.cdn.bcebos.com/pic/9d82d158ccbf6c81ddd35ae7b63eb13532fa40dc?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UxMTY=,xp_5,yp_5',
        'https://bkimg.cdn.bcebos.com/pic/80cb39dbb6fd52665f904a1ba118972bd4073601?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UxMTY=,xp_5,yp_5',
        'https://bkimg.cdn.bcebos.com/pic/e850352ac65c10383f331056b8119313b17e89d1?x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2U4MA==,xp_5,yp_5'
    ]
    p1 = Process(target=download, args=(images, q1))
    p2 = Process(target=save_file, args=(q1,))

    start = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print('用时：{}秒'.format(end - start))
