from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '10'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'YAL-AL00'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'com.znb.zxx'               # app的名字：
                                                        # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                       # 安卓8.1之后：adb shell dumpsys activity | findstr "mResue"
                                                    #    adb shell dumpsys package XXX[com.znb.zxx]   查看某个包的具体信息
desired_caps['appActivity'] = '.pages.splash.SplashActivity'              # 同上↑
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
# 去打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) 



driver.find_element_by_android_uiautomator('new UiSelector().text("密码登录")').click()