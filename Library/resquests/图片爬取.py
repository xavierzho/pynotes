import requests
import os

root = "C:/Users/77545/Pictures/Saved Pictures"

url = "http://img0.dili360.com/ga/M00/46/FC/wKgBy1iv0WmAaXa1AE7LkZQs2kI077.tub.jpg@!rw9"
path = root + url.split('/')[-1]
# print(r.status_code)
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")

