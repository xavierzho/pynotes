import time
import redis
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

r = redis.Redis('127.0.0.1', 6379)


def toutiao_save_and_preview(title, content, expand_link):
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        executable_path='C:\selenium_chromedriver\chromedriver.exe',
        chrome_options=option
    )
    driver.get('')
