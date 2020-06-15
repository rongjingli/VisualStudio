from selenium import webdriver
import unittest, time
from po.LoginPage import LoginPage
from po.IndexPage import IndexPage
from utils.filetools import save
from utils.filetools import read


# 类的继承
@unittest.skip("不要想让他执行")
class TestCaseLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver= webdriver.Chrome(executable_path='driver/chromedriver.exe')
        # cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print("测试用例开始!")
        self.driver.get('http://193.112.79.96:8080/ljindex/index.html')
        
    def tearDown(self):
        print("测试用例结束!")

    def test_01_login(self):
        """ 业务逻辑, 首页--->登陆-->首页 """
        indexpage = IndexPage(self.driver)
        indexpage.go_login_page()  
        time.sleep(3)
        # 实例化登录页面
        loginpage = LoginPage(self.driver)
        loginpage.login("zhangsan","12345678")
        time.sleep(3)
        self.assertEqual(self.driver.title,indexpage.title)

