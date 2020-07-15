# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.1.2"
caps["deviceName"] = "V1938T"
caps["appPackage"] = "com.znb.zxx"
caps["appActivity"] = ".pages.splash.SplashActivity"
caps["unicodeKeyboard"] = True
caps["resetKeyboard"] = True
caps["autograntpermissions"] = True
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.znb.zxx:id/navigator_mine_view")
el1.click()
el2 = driver.find_element_by_id("com.znb.zxx:id/user_nickname_view")
el2.click()
el3 = driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc=\"密码登录\"]/android.widget.TextView")
el3.click()
el4 = driver.find_element_by_id("com.znb.zxx:id/phone_edit_view")
el4.send_keys("15801180856")
el5 = driver.find_element_by_id("com.znb.zxx:id/pwd_edit_view")
el5.send_keys("Jing12345678")
el6 = driver.find_element_by_id("com.znb.zxx:id/confirm_view")
el6.click()

driver.quit()