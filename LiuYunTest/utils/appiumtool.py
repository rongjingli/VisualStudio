from appium import webdriver


def get_driver():    
    desired_caps = {}
    desired_caps['platformName'] = 'Android'                    
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = 'V1938T'
    desired_caps['appPackage'] = 'com.allsaprk.dh.allspark'
    desired_caps['appActivity'] = '.activity.MainActivity'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True 
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver