import requests
url = "https://www.amazon.cn/dp/B00G4JPDJO?ref_=Oct_RecCard_dsk_asin2&pf_rd_r=2G0A5WS9Q7DKFB4TATM2&pf_rd_p=d7526bc5-3640-48d5-8d6b-448fefacc51e&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-4"
kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
r = requests.get(url, headers=kv)
# print(r.status_code)
r.encoding = r.apparent_encoding
# print(r.request.headers)  # 向亚马逊发送的信息内容
print(r.text[:1000])
