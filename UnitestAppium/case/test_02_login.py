import unittest
import time
# 1.导入appium的webdriver
from appium import webdriver
from utils.appiumtools import get_driver
from po.test_01_IndexPage import IndexPage
from po.test_02MinePage import MinePage
from po.LoginPage import LoginPage
from po.InformationPage import InformationPage

# 类的继承
# @unittest.skip("不")


class TestCaseLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        print("启动驱动!")

    @classmethod
    def tearDownClass(cls):
        print("关闭驱动!")
        cls.driver.quit()

    def setUp(self):

        print("测试用例开始!")
        # 首页
        indexpage = IndexPage(self.driver)
        indexpage.go_mine_view()
        time.sleep(3)
        # 实例化我的页面
        minePage = MinePage(self.driver)
        minePage.login()
        username = self.driver.find_element_by_id(
            "com.znb.zxx:id/user_nickname_view").text
        if username != minePage.username:
            self.test_01_login()

    def tearDown(self):
        self.test_performance()
        print("测试用例结束!")

    def test_01_login(self):
        # 实例化登录页面
        loginpage = LoginPage(self.driver)
        u = "15801180856"
        p = "Jing12345678"
        loginpage.Pwdlogin(u, p)
        username = self.driver.find_element_by_id(
            "com.znb.zxx:id/user_nickname_view").text
        print(username)
        print("打印:")
        time.sleep(3)
        # 断言用户名158****0856
        self.assertEqual(username, '158****0856')

    def test_02_information(self):
        nickname_text = "你好"
        # 实例化登录页面-->进入账号中心
        loginpage = LoginPage(self.driver)
        loginpage.go_information()
        # 实例化账号中心页面
        informationPage = InformationPage(self.driver)
        informationPage.update_nickname(nickname_text)

    def test_performance(self):
        """ 
            统计app  cpu使用率 耗电量 等信息
            可以作为最后一个case来完成 
        """
        print(self.driver.get_performance_data_types())
        for p in self.driver.get_performance_data_types():
            try:
                print(self.driver.get_performance_data(
                    "io.appium.android.apis", p, 5))
            except:
                pass
