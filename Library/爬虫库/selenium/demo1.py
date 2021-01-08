import time
# 与百度首页交互
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


option = webdriver.ChromeOptions()
# option.add_argument('headless')

# 要换成适应自己的操作系统的chromedriver

driver = webdriver.Chrome(
    executable_path='D:/Devtools/ChromeDriver/chromedriver.exe',
    chrome_options=option
)

url = 'https://www.baidu.com'
# 打开网站
driver.get(url)
# 打印当前页面的标题
driver.implicitly_wait()
print(driver.title)

timeout = 5
# 调用输入框，输入python
search_content = WebDriverWait(driver, timeout).until(
    lambda d: d.find_element_by_id('kw'))
search_content.send_keys('python')


# 模拟点击‘百度一下’
search_button = WebDriverWait(driver, timeout).until(
    lambda d: d.find_element_by_xpath('//input[@id="su"]'))
search_button.click()
time.sleep(3)
# 页面截图
# driver.save_screenshot('baidu.png')

# 打印搜索结果
search_results = WebDriverWait(driver, timeout).until(
    lambda d: d.find_elements_by_xpath('//h3[contains(@class,"t")]/a[1]')
)

# 获取渲染后的数据
print('获取渲染后的数据:{}'.format(driver.page_source))
# 查看渲染后的cookies
print('获取渲染后的cookies:{}'.format(driver.get_cookies()))
# 查看当前页面的路径
print('渲染后的url:{}'.format(driver.current_url))

# for item in search_results:
#     print(item.text)

# driver.close()  # 关闭页面
# driver.quit()  # 关闭浏览器
