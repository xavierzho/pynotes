import requests
url = "http://m.ip138.com/ip.asp?ip="
r = requests.get(url + "59.41.188.161")
print(r.status_code)
