from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


option = webdriver.ChromeOptions()
option.add_argument('headless')

# 要换成适应自己的操作系统的chromedriver

driver = webdriver.Chrome(
    executable_path='D:/Devtools/ChromeDriver/chromedriver.exe',
    chrome_options=option
)

url = 'https://www.toutiao.com/'
# 打开网站
driver.get(url)
# 打印当前页面源码
print(driver.page_source)

timeout = 5
coin_links = WebDriverWait(driver, timeout).until(
    lambda d: d.find_elements_by_xpath('//div[@ga_event="video_item_click"]/a'))

for item in coin_links:
    print(item.text)
    print(item.get_aaribute('href'))
