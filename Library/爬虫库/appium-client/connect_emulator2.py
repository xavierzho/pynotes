from appium import webdriver
import time

desired_caps = {
    "platformName": "Android",  # 检测手机系统是安卓,IOS
    "platformVersion": "5.1.1",  # 安卓版本
    "deviceName": "shamu",  # 设备名，安卓可以留空
    "appPackage": "com.android36kr.app",  # 启动APP Package名
    "appActivity": ".ui.LogoActivity",  # 启动Activity名称
    "unicodeKeyboard": True,  # 使用自带输入法，输入中文时候填True
    "resetKeyboard": True,  # 执行完程序回复原来输出法
    "noReset": True,  # 不要重置App
    "UDID": "127.0.0.1:62001",
    "newCommandTimeout": 6000,
    "automationName": "UiAutomator2",  #
    # 'app': r'本机目录'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)
driver.implicitly_wait(8)


# driver.find_element_by_android_uiautomator('new UiSelector().text("快讯")').click()
# el1 = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android36kr.app:id/item_news_up_title").index(0)')
# driver.find_element_by_android_uiautomator('new UiSelector().text("展开").index(1)').click()
# el2 = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android36kr.app:id/item_news_up_title").index(0)')
# driver.scroll(el1, el2)

