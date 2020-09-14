from appium import webdriver
from time import sleep


desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "shamu",
    "appPackage": "com.android36kr.app",
    "appActivity": ".ui.LogoActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset": True,
    "newCommandTimeout": 6000,
    "automationName": "UiAutomator2",
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)
sleep(5)
driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
verify = driver.find_element_by_android_uiautomator('new UiSelector().text("登录关注")')

if verify:
    verify.click()

    driver.find_element_by_android_uiautomator('new UiSelector().text("账号密码登录")').click()

    driver.find_element_by_android_uiautomator('new UiSelector().text("输入手机号")').send_keys("15913101814")
    driver.find_element_by_id('com.android36kr.app:id/login_input_password').send_keys("Snq1997.")
    login_button = driver.find_element_by_id('com.android36kr.app:id/login_input_action')
    if login_button.get_attribute("enabled") == "true":
        login_button.click()
        driver.find_element_by_id("com.android36kr.app:id/c_back").click()
    else:
        print('内容输入不正确')
else:
    print('已经登录')



sleep(5)
driver.quit()


