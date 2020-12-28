"""
@Author: Jonescyna@gmail.com
@Created: 2020/12/23
"""
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.support import expected_conditions as ec
import time

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('-disable-images')

options.add_argument('-disable-gpu')
options.add_argument('-start-maximized')
driver = webdriver.Chrome(options=options, executable_path='D:/WebDriver/chromedriver.exe')
# driver.set_window_size(configure.windowHeight, configure.windowWidth)
category_url = 'https://www.amazon.cn/b/ref=s9_acss_bw_cg_pccateg_2a1_w?node=106200071&pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-2&pf_rd_r=PQNKPPABQXAWCTZSNFXA&pf_rd_t=101&pf_rd_p=cdcd9a0d-d7cf-4dab-80db-2b7d63266973&pf_rd_i=42689071'
driver.get(category_url)
# [@id!="cat1"][@id!="cat2"]
# category_list = driver.find_elements_by_xpath('//div[starts-with(@id,"cat")][@id!="cat1"][@id!="cat2"]//div[@class="a-row a-spacing-small"]')
# category_dict = {}
# small_category = {}
# for i in category_list:
#     category_dict['main_category'] = i.find_element_by_xpath('./span/a').text
#     category_dict['main_category_link'] = i.find_element_by_xpath('./span/a').get_attribute('href')
#     category_dict['categories'] = []
#     for j in i.find_elements_by_xpath('//li[@class="a-spacing-small"]/span/span'):
#         small_category['category'] = j.find_element_by_xpath('./a').text
#         small_category['category_link'] = j.find_element_by_xpath('./a').get_attribute('href')
