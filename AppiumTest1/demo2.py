from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '7.1.2'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'V1938T'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'io.appium.android.apis'               # app的名字：
                                                        # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                        # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
desired_caps['appActivity'] = '.ApiDemos'              # 同上↑
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
# 去打开app，并且返回当前app的操作对象
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id('com.allsaprk.dh.allspark:id/et_user').send_keys('18408223928')
driver.find_element_by_id('com.allsaprk.dh.allspark:id/et_pass').send_keys('a12345678')
driver.find_element_by_id('com.allsaprk.dh.allspark:id/bt_login').click()
time.sleep(3)
driver.find_element_by_id('com.allsaprk.dh.allspark:id/rl_right').click()
time.sleep(3)
driver.find_element_by_id('com.allsaprk.dh.allspark:id/et_search').send_keys('a')
e =driver.find_element_by_android_uiautomator('new UiSelector().text("佛系投资")')
assert e.text=="佛系投资"
print("通过")




