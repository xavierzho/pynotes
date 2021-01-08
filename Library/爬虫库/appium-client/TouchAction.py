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

sleep(3)
# ----------轻巧
# element = driver.find_element_by_android_uiautomator('new UiSelector().text("WLAN")')
# TouchAction(driver).tap(x=75, y=300).perform()

# ----------按下和抬起
TouchAction(driver).press(x=100, y=130).release().press().wait(2000).perform()
sleep(2)
# TouchAction(driver).release(x=100, y=130).perform()
driver.quit()
