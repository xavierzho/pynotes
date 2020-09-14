from time import sleep
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "shamu",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": True,
    "newCommandTimeout": 6000,
    "automationName": "UiAutomator2",
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)
# 隐式等待--------------------
# driver.implicitly_wait(10)

# 显示等待--------------------


# print("--准备找返回进行点击")
# wait = WebDriverWait(driver, 25, 5)
# back_button = wait.until(lambda x: x.find_element_by_android_uiautomator('new UiSelector().description("收起")'))
# back_button.click()
# print("--点击完了")

# 获取元素的位置和大小
search_button = driver.find_element_by_id()
sleep(5)
driver.quit()
