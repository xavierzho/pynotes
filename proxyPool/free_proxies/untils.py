import requests


def get_page(url):
    headers = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,'
                             'likeGecko)Chrome/83.0.4103.116Safari/537.36'}
    r = requests.get(url, headers=headers)
    return r.text


def get_context(url):
    headers = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,'
                             'likeGecko)Chrome/83.0.4103.116Safari/537.36'}
    r = requests.get(url, headers=headers)
    return r.content.decode()






