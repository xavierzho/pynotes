import requests

# 请求数据的url
member_url = 'https://www.yaozh.com/member/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
# 需要cookies 的字典类型
cookie_dict = {
    'PHPSESSID': '2m03t772er6t9ogcj3mu2lvp17',
    '_ga': 'GA1.2.845391702.1595156220',
    '_gid': 'GA1.2.339085681.1595156220',
    'acw_tc': '2f624a1915951693144652254e383a93b53c211760759a82522b8bbc7ae327',
    '_gat': '1',
    'Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94': '1595169389',
    'yaozh_logintime': '1595169389',
    'yaozh_user': '956358%09TinsQua',
    'yaozh_userId': '956358',
    'yaozh_jobstatus': 'kptta67UcJieW6zKnFSe2JyXnoaabJtompyHnKZxanJT1qeSoMZYoNdzbptahszT1bLZxYNy2G%2BenofNlKqpl6XKppZVnKmflWlxg2lnnJqfd32FFea439789D751c1E6CEEA44b1C3TlpqWkWuHcNiemZtVq56lloN0pG2SaZ%2BGamyabWOZnpWalJaSa4dw4g%3D%3D246be4b908d948937fc968d21008be35',
    'db_w_auth': '800021%09TinsQua',
    'UtzD_f52b_saltkey': 'gZBw8DGW',
    'UtzD_f52b_lastvisit': '1595165790',
    'UtzD_f52b_lastact': '1595169390%09uc.php%09',
    'UtzD_f52b_auth': '8e44miKPc6UAwljnj3CCYupDLxJtylZO1lUxGxnD3nH%2F8ssNtFy0ag1LDozOJLfV948n9jiwoavLwGJjqivUuGvkIkY',
    'yaozh_uidhas': '1',
    'yaozh_mylogin': '1595169392',
    'acw_tc': '2f624a1915951693144652254e383a93b53c211760759a82522b8bbc7ae327',
    'Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94': '1595154612%2C1595156220%2C1595169318'
}

response = requests.get(url=member_url, headers=headers, cookies=cookie_dict)

data = response.content.decode()

with open('cookies.html', 'w', encoding='utf-8') as f:
    f.write(data)
