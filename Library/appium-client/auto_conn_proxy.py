from appium import webdriver
from time import sleep
from appium.webdriver.extensions.action_helpers import TouchAction

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

sleep(1)

TouchAction(driver).press(x=120, y=180).release().long_press(x=120, y=180).perform()
checked = driver.find_element_by_android_uiautomator('new UiSelector().text("修改网络")')

if checked.get_attribute("checked") == "true":
    checked.click()
    for i in ["高级选项", "无", "手动"]:
        driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(i)).click()
    host = driver.find_element_by_id('com.android.settings:id/proxy_hostname')
    TouchAction(driver).tap(host).perform()
    host.send_keys("192.168.101.103")
    port = driver.find_element_by_id('com.android.settings:id/proxy_port')
    TouchAction(driver).tap(port).perform()
    port.send_keys('9000')
    save_button = driver.find_element_by_android_uiautomator('new UiSelector().text("保存")')

    if save_button.get_attribute('enabled') == 'true':
        save_button.click()
else:
   pass

sleep(1)

driver.quit()

