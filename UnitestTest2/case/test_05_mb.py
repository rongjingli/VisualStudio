import unittest
import time
from selenium import webdriver
from utils.seleniumtools import auto_login
from po.MbPage import MbPage


# 类的继承
@unittest.skip("不要想让他执行")
class TestCaseMB(unittest.TestCase):
    """ 个人信息页面 """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='driver/chromedriver.exe')
        # cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        """ 业务逻辑, 首页--->登陆-->个人信息页面 """
        print("测试用例开始!")
        self.driver.get('http://49.232.185.181:8080/ljindex/index.html')
        auto_login(self.driver)
        time.sleep(3)
        # 调用判断自动登陆
        # 主页点击用户头像跳转个人信息页面
        self.driver.find_element_by_id('personal').click()
        time.sleep(3)
    def tearDown(self):
        print("测试用例结束!")


    def test_02_mb(self):

        """ 密保 """
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[2]/div[1]/div[7]').click()
        usertitle = self.driver.title    
        mbPage = MbPage(self.driver)
        p = "12345678"
        a1 = "嘻嘻嘻"
        a2 = "哈哈哈"
        a3 = "哈哈哈"
        mbPage.Mbuser(p, a1, a2, a3)
        self.assertEqual(usertitle, mbPage.title)
        print("设置密保结束!")


