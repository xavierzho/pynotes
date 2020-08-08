from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


option = webdriver.ChromeOptions()
# option.add_argument('headless')

# 要换成适应自己的操作系统的chromedriver

driver = webdriver.Chrome(
    executable_path='C:\selenium_chromedriver\chromedriver.exe',
    chrome_options=option
)

url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=rowdata'
# 打开网站
driver.get(url)
# 打印当前页面源码
print(driver.title)

timeout = 5
link = WebDriverWait(driver, timeout).until(
    lambda d: d.find_element_by_link_text('一行数据'))
link.click()

# 切换页面
window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])

article_links = WebDriverWait(driver, timeout).until(
    lambda b: b.find_elements_by_xpath('//h4[@class="weui_media_title"]')
)
article_links_list = []
for item in article_links:
    article_link = 'http://mp.weixin.qq.com'+ item.get_attribute('hrefs')
    article_links_list.append(article_link)

print(article_links_list)

first_article_link = article_links_list[0]

import requests
from lxml import etree

headers = {
    'Accept': ''
}