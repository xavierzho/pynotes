# coding=utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from lxml import etree

url = "http://www.hotstar.com/movies/languages/kannada/"
driver = webdriver.PhantomJS(executable_path=r"phantomjs")
# driver = webdriver.Firefox
driver.get(url)
time.sleep(5)

link_len_list = []
while True:
    driver.execute_script('window.scrollTo(0,1000000)')
    time.sleep(3)
    html = driver.page_source
    html = etree.HTML(html.encode("utf-8", 'ignore'))
    items = html.xpath("//div[contains(@class, 'rec-received')]/div/hs-cards-directive/article/a/@href")
    # print(title, '----------------2------------------')
    for item in items:
        print(item)

    link_len = len(items)
    print(link_len)
    link_len_list.append(link_len)
    if len(link_len_list) > 1:
        print(link_len_list[-1])
        print(link_len_list[-2])
        print('----------------')
        if link_len_list[-1] == link_len_list[-2]:
            print('渲染完成')
            break

driver.quit()