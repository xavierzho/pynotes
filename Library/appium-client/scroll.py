from time import sleep
from appium import webdriver

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

sleep(8)

more_button = driver.find_element_by_android_uiautomator('new UiSelector().text("更多")')
app_button = driver.find_element_by_android_uiautomator('new UiSelector().text("应用")')
# driver.scroll(app_button, more_button, 2000)
driver.drag_and_drop(app_button, more_button)

sleep(3)
driver.quit()

