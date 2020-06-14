from selenium.webdriver.support.ui import WebDriverWait
import time

def find_element(driver, locator, timeout=60):
    """
        方法名：显示等待，动态取查找元素
        参数：
            driver：浏览器句柄/把柄
            locator:元素的定位方式和值
                格式：
                    - ("id", "username")
                    - ("xpath", "xxxxxxx")
                    - ("name", "xxxxxx")
                    - ("css selector", "xxxxx")
                    - ("class name", "xxxxxxxx")
                    - ("link text", "抗击肺炎")
                    - ("partial link text", "抗击肺")
            timeout:查找元素的超时，默认60S
        返回值：
            - 到找元素：返回元素
            - 没找到元素：直接报错
    """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))


def assert_element_exist(driver, locator, timeout=60):
    """
        方法名：判断元素是否存在
        参数：
            driver：浏览器句柄/把柄
            locator:元素的定位方式和值
                格式：
                    - ("id", "username")
                    - ("xpath", "xxxxxxx")
                    - ("name", "xxxxxx")
                    - ("css selector", "xxxxx")
                    - ("class name", "xxxxxxxx")
                    - ("link text", "抗击肺炎")
                    - ("partial link text", "抗击肺")
            timeout:查找元素的超时，默认60S
        返回值：
            - 元素存在：返回True
            - 元素不存在：返回False
    """
    try:
        find_element(driver, locator, timeout)
        return True
    except:
        return False

# 登陆按钮存在就自动登陆
def auto_login(driver):
    
    login_status = ('link text', '登录')
    # 元素存在没有
    if assert_element_exist(driver, login_status) == True:
        # 要去登录
        find_element(driver, login_status).click()
        time.sleep(3)
        username = ('id', 'username')
        password = ('id', 'password')
        loginbtn = ('id', 'userLogin')
        find_element(driver, username).send_keys("cwx123")
        find_element(driver, password).send_keys("12345678")