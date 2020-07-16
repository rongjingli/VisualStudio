from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

def get_driver():
    """
        获取设备driver
    """
    # 手机和app的信息
    desired_caps = {}
    desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
    desired_caps['platformVersion'] = '7.1.2'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
    desired_caps['deviceName'] = 'V1938T'                       # 手机/模拟器的型号：adb shell getprop ro.product.model
    desired_caps['appPackage'] = 'com.znb.zxx'               # app的名字：adb shell dumpsys package XXX 
    desired_caps['appActivity'] = '.pages.splash.SplashActivity'              # 同上↑  # .pages.splash.SplashActivity   pages.main.MainActivity

    desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
    desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
    desired_caps['noReset'] = True                      # 使用app的缓存
    desired_caps['autograntpermissions'] = True                      # 使用app的权限自动开启

    # 去打开app，并且返回当前app的操作对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    return driver






def find_element(driver, locator, timeout=30):
    """
        方法名：diy查找元素
        参数：
            driver: 浏览器的句柄/把柄
            locator: 元素定位方式
                格式： 
                    - find_element_by_id：("id", "value") find_element_by_id > resource_id
                    - find_element_by_xpath：("xpath", "value")
                    - find_element_by_accessibility_id：("aid", "value")
                    - find_element_by_android_uiautomator：("text", "Search")
            timeout: 超时间时间，默认10
        返回值：
            - 找到元素：返回元素
            - 没找到元素：直接报错
    """
    if locator[0] == "aid":
        locator = ("accessibility id", locator[1]) # locator:appium能够识别""" """  """ """
    if locator[0] == "text":
        locator = ("-android uiautomator", 'new UiSelector().text("{}")'.format(locator[1]))

    return WebDriverWait(driver,timeout=30).until(lambda x:x.find_element(*locator))



def is_element_exist(driver, locator, timeout):
    """
    timeout=30
        方法名：判断元素是否存在
        参数：
            driver: 浏览器的句柄/把柄
            locator: 元素定位方式
                格式： 
                    - find_element_by_id：("id", "value") find_element_by_id > resource_id
                    - find_element_by_xpath：("xpath", "value")
                    - find_element_by_accessibility_id：("aid", "value")
                    - find_element_by_android_uiautomator：("text", "Search")
            timeout: 超时间时间，默认10
        返回值：
            - 找到元素：true
            - 没找到元素：false
    """
    try:
        find_element(driver, locator, timeout)
        # WebDriverWait(driver,timeout).until(lambda x:x.find_element(*locator))
        return True
    except:
        return False