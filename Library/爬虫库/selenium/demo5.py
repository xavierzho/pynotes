from selenium import webdriver
from time import sleep
option = webdriver.ChromeOptions()
# option.add_argument('headless')

driver = webdriver.Chrome(
    executable_path='D:/Devtools/ChromeDriver/chromedriver.exe',  # 浏览器driver所在的绝对路径
    chrome_options=option
)
url = 'https://www.pearvideo.com/category_8'
driver.get(url)


# 通过标签id值取标签对象
res1 = driver.find_element_by_id('actSearch')
# print(res1)
# 通过标签的class属性获取标签对象
res2 = driver.find_elements_by_class_name('categoryem')
# print(res2)
# 通过标签包裹的文本 获取元素列表（精准定位）
res3 = driver.find_element_by_link_text('下载APP')
# print(res3)
# 通过标签包裹的文本 获取元素列表（模糊定位）
res4 = driver.find_elements_by_partial_link_text('科技')
# print(len(res4))
# 通过标签名获取元素列表
res5 = driver.find_elements_by_tag_name('li')

"""
driver.find_element_by_xpath('//*[@id="listvideoListUl"]/li[1]/div/a').click()

# 获取当前所有的窗口
current_window = driver.window_handles
print(current_window)
# 切换窗口
driver.switch_to.window(current_window[1])

# 前进 和 回退 的操作
driver.back()  # 后退
driver.forward()  # 前进

# 进入嵌套网页（实现自动登录）
driver.switch_to_frame(0)
# 处理弹框
driver.switch_to_alert()
"""
for i in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight); "
                          "var lenOfPage=document.body.scrollHeight; return lenOfPage")
    driver.find_element_by_xpath('//*[@id="listLoadMore"]').click()
    if driver.find_element_by_xpath('//*[@id="listLoadMore"]').text == '没有更多内容':
        break
