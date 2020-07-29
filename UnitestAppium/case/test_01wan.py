import unittest
import time
from appium import webdriver

# 类的继承
# @unittest.skip("不")

class TestCaseWan(unittest.TestCase):

    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "7.1.2"
    caps["deviceName"] = "V1938T"
    caps["appPackage"] = "com.znb.zxx"
    caps["appActivity"] = ".pages.splash.SplashActivity"
    caps["unicodeKeyboard"] = True
    caps["resetKeyboard"] = True
    caps["noReset"] = True
    caps["autoGrantPermissions"] = True

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    el1 = driver.find_element_by_id("com.znb.zxx:id/navigator_mine_view")
    # el1 = driver.find_element_by_android_uiautomator('new UiSelector().text("我的")')
    el1.click()

    time.sleep(3)
    el2 = driver.find_element_by_id("com.znb.zxx:id/user_nickname_view")
    el2.click()
    time.sleep(3)
    el3 = driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc=\"密码登录\"]/android.widget.TextView")
    el3.click()
    time.sleep(1)
    el3.send_keys("15801180856")
    el4 = driver.find_element_by_id("com.znb.zxx:id/pwd_edit_view")
    el4.send_keys("Jing12345678")
    el5 = driver.find_element_by_id("com.znb.zxx:id/confirm_view")
    el5.click()
    time.sleep(3)
    print("结束")
    driver.quit()

if __name__ == '__main__':
    unittest.main()