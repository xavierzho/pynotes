# 案例 asyncio +不支持异步的模块
import asyncio
import requests


async def download_image(url):
    print('开始下载：', url)

    loop = asyncio.get_event_loop()

    future = loop.run_in_executor(None, requests.get, url)

    response = await future
    print('下载完成')
    file_name = url.rsplit('_')[-1]
    with open(file_name, 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    url_list = ['http://wx4.sinaimg.cn/bmiddle/ae2c6e1dly1ghbrx9se5qg20g20c27lq.gif', 'http://wx2.sinaimg.cn/bmiddle/ab4b8062gy1gh5yoq4nhij20u00u010r.jpg', 'http://wx2.sinaimg.cn/bmiddle/006GJQvhgy1gfw8qggsu9j30u00u0q51.jpg', 'http://wx1.sinaimg.cn/bmiddle/006dMd5bgy1gh6jvxsd3dj30u00u00wa.jpg', 'http://wx2.sinaimg.cn/bmiddle/005PeXV6gy1gh5vffj3j9j30ix0i1gn8.jpg', 'http://wx3.sinaimg.cn/bmiddle/de80a5abgy1gg081fts03g208c04o7de.gif', 'http://wx1.sinaimg.cn/bmiddle/005TGG6vly1ghbilmq4wij30u00u00tx.jpg', 'http://wx3.sinaimg.cn/bmiddle/0088UfVOgy1ghcgkgurv0j31kw1kw4qp.jpg', 'http://wx4.sinaimg.cn/bmiddle/007bCYcngy1gh713u0unoj30j60hh752.jpg', 'http://wx4.sinaimg.cn/bmiddle/78b88159ly1ghbay41w58g20dc0dcjsh.gif', 'http://wx1.sinaimg.cn/bmiddle/b64da6adly1gh5qktg3etg208x08xh7z.gif', 'http://wx2.sinaimg.cn/bmiddle/b64da6adly1gh5qktl80qg208c08ch5a.gif', 'http://wx3.sinaimg.cn/bmiddle/ab4b8062gy1gh5yowep5ij20ox0f9q58.jpg', 'http://wx1.sinaimg.cn/bmiddle/b64da6adly1ggyhqm0b0bj20j60j53zx.jpg', 'http://wx3.sinaimg.cn/bmiddle/005TGG6vly1ghbilkl472j30c80c8dgh.jpg', 'http://wx1.sinaimg.cn/bmiddle/c3335c0ely1ghb2xglyfnj202s02da9u.jpg', 'http://wx1.sinaimg.cn/bmiddle/0065btHFly1gh70qkah2sg302s02sglg.gif', 'http://wx3.sinaimg.cn/bmiddle/ab4b8062gy1gh5yovocmfj20qo0qoabv.jpg', 'http://wx2.sinaimg.cn/bmiddle/007bCYcngy1ghe199m73wj30sg0sgjud.jpg', 'http://wx2.sinaimg.cn/bmiddle/ceeb653ely1ghdt2fj8kbg208c08c4oe.gif', 'http://wx1.sinaimg.cn/bmiddle/006I1bcHly1ghcqaeehxjj30j80j6q4r.jpg', 'http://wx2.sinaimg.cn/bmiddle/0065btHFly1gh70qk1sevg302s02sa9w.gif', 'http://wx3.sinaimg.cn/bmiddle/ab4b8062gy1gh5yoplogjj20u00u0q6c.jpg', 'http://wx1.sinaimg.cn/bmiddle/006qOO1Xgy1gggiamfxo9j30hs0hs75u.jpg', 'http://wx1.sinaimg.cn/bmiddle/006APoFYly1ghe0w3wkz2g304704q0tk.gif', 'http://wx2.sinaimg.cn/bmiddle/005PeXV6gy1gh3lis8s7sj30u00u041o.jpg', 'http://wx1.sinaimg.cn/bmiddle/ab4b8062gy1ggyir71hezj20no0v879j.jpg', 'http://wx4.sinaimg.cn/bmiddle/006CXrEjly1gfymwmoc2nj30u00tgwgm.jpg', 'http://wx3.sinaimg.cn/bmiddle/006dMd5bgy1gh6jw21tygj30j60j6dkl.jpg', 'http://wx4.sinaimg.cn/bmiddle/b64da6adly1gh5iysc57lj20c80c8dg8.jpg', 'http://wx2.sinaimg.cn/bmiddle/b64da6adly1gh5qkthql8g206006kdrn.gif', 'http://wx2.sinaimg.cn/bmiddle/a8a1efafly1gh3h1684xej20sg0sg76x.jpg', 'http://wx4.sinaimg.cn/bmiddle/005PeXV6gy1gh3lir37zlj30n00mkdkf.jpg', 'http://wx3.sinaimg.cn/bmiddle/0073Cjx6gy1gghh274u9zj306o06odg8.jpg', 'http://wx4.sinaimg.cn/bmiddle/006C7PHRly1ggexqolw8tg30a00a0e81.gif', 'http://wx4.sinaimg.cn/bmiddle/ab4b8062gy1gfz0o4aljkj20dj0d40tm.jpg', 'http://wx1.sinaimg.cn/bmiddle/006C7PHRly1gghherk338j30c80c83yt.jpg', 'http://wx3.sinaimg.cn/bmiddle/006qOO1Xgy1gggiak33j6g306o06ognt.gif', 'http://wx2.sinaimg.cn/bmiddle/006I1bcHgy1ggey7c3k8kj308c07zdg8.jpg', 'http://wx2.sinaimg.cn/bmiddle/0073Cjx6gy1ggytse5236j301j01j0sq.jpg', 'http://wx3.sinaimg.cn/bmiddle/007k5D43ly1ghao7j5ro9j30dw0dpweu.jpg', 'http://wx1.sinaimg.cn/bmiddle/006mMMLigy1ghanxlf76bj305i05idg9.jpg', 'http://wx2.sinaimg.cn/bmiddle/b64da6adly1gh5qpkzpfgg2058058wlo.gif', 'http://wx2.sinaimg.cn/bmiddle/b64da6adly1gh5qpljr0lg208d09skgi.gif', 'http://wx1.sinaimg.cn/bmiddle/006mMMLigy1ggxwb7vkddj30hs0hsdhc.jpg']
    tasks = [download_image(url) for url in url_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
