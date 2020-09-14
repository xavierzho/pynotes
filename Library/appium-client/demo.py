from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey


desired_caps = {
    "platformName": "Android",  # 检测手机系统是安卓,IOS
    "platformVersion": "9",  # 安卓版本
    "deviceName": "dreamqltechn",  # 设备名，安卓可以留空
    "appPackage": "tv.danmaku.bili",  # 启动APP Package名
    "appActivity": "ui.splash.SplashActivity",  # 启动Activity名称
    "unicodeKeyboard": True,  # 使用自带输入法，输入中文时候填True
    "resetKeyboard": True,  # 执行完程序回复原来输出法
    "noReset": True,  # 不要重置App
    "newCommandTimeout": 6000,
    "automationName": "UiAutomator2",  #
    # 'app': r'本机目录'
}


# 连接Appium Server 初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)
# 设置缺省等待时间
driver.implicitly_wait(5)
# 同意用户协议
# agree = driver.find_element_by_id('agree')
# if agree:
#     agree.click()

# driver.find_element_by_id('tab_text')
# driver.find_e
# 模拟登录
# driver.find_element_by_id('avatar').click()
# if driver.find_element_by_id('nick_name').text:
#     tag = driver.find_element_by_id('tab_text').text
#     if tag == '首页':
#         tag.click()
# else:
#     driver.find_element_by_id('tv_submit').click()

# 根据id定位搜索框，点击
driver.find_element_by_id('tv.danmaku.bili:id/expand_search').click()
sbox = driver.find_element_by_id('search_src_text')
sbox.send_keys('白月黑羽')
# 输入回车键，确定搜索元素
driver.press_keycode(AndroidKey.ENTER)

# 选择定位所有视频标题
elements = driver.find_elements_by_id('title')

for element in elements:
    print(element.text)

input('q')
driver.quit()
