import time
import redis
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# r = redis.Redis('127.0.0.1', 6379)

# 实现自动登录豆瓣
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path='D:/Devtools/ChromeDriver/chromedriver.exe',
    chrome_options=option
)
driver.get('https://www.douban.com/')
# 进入嵌套网页
driver.switch_to_frame(0)

driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()

driver.find_element_by_xpath('//*[@id="username"]').send_keys('15913101814')

driver.find_element_by_xpath('//*[@id="password"]').send_keys('Snq1997.')

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()


