import unittest, time
# 1.导入appium的webdriver
from appium import webdriver
from utils.appiumtools import is_element_exist
from utils.appiumtools import get_driver

# 类的继承
@unittest.skip("不")
class Lianxi(unittest.TestCase):
    def setUp(self):
        self.driver =  get_driver()
        print("测试用例开始!") 

    def tearDown(self):
        self.driver.quit()
        print("测试用例结束!")

    def test_01_dingwei(self):
        self.course =("class name","android.widget.TextView")
        # self.course =("id","com.znb.zxx:id/home_search_view")
        el= is_element_exist(self.driver, self.course, 30)
        print("打印")
        print(el)
        print("打印")
         


