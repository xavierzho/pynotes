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

sleep(8)


def swipe_down():
    titles = driver.find_elements_by_id('com.android36kr.app:id/item_news_up_title')[1]
    coordinate = titles.get_attribute('bounds')
    coordinate = eval(coordinate.replace('][', '],['))
    x = coordinate[1][0]
    y = coordinate[1][1]
    driver.swipe(x, y, 522, 110, 4000)


def get_info():
    title = driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.android36kr.app:id/item_news_up_title")')
    title.click()
    info = {
        'title': title.text,
        'description': driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.android36kr.app:id/item_news_up_content")').text
    }
    return info


if __name__ == '__main__':
    lis = []
    num = 0
    while 1:
        driver.find_element_by_android_uiautomator('new UiSelector().text("快讯")').click()

        lis.append(get_info())
        num += 1
        swipe_down()
        print('正在爬取第%d个' % num)
        if not lis.append(get_info()):
            break
