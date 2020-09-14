from appium import webdriver
from time import sleep
from appium.webdriver.extensions.action_helpers import TouchAction
from appium.webdriver.connectiontype import ConnectionType
import os
from appium.webdriver.extensions.android.nativekey import AndroidKey


desired_caps = dict()
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1.1"
desired_caps["deviceName"] = "shamu"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".ChooseLockPattern"
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
desired_caps["noReset"] = True
desired_caps["newCommandTimeout"] = 6000
desired_caps["automationName"] = "UiAutomator2"


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)
sleep(3)
TouchAction(driver).press(x=90, y=300).move_to(x=270, y=300).move_to(x=450, y=300).move_to(x=450, y=480).perform()
# driver.get_screenshot_as_file(os.getcwd()+os.sep+'./screen.png')
print(driver.network_connection)
driver.set_network_connection(6)

driver.open_notifications()

AndroidKey.BACK()

input('任意按键退出')

driver.quit()

