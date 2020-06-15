from selenium import webdriver
import unittest, time
from po.IndexPage import IndexPage
from po.RegistPage import RegistPage
from po.LoginPage import LoginPage

@unittest.skip("不要想让他执行")
class TestCaseRegist(unittest.TestCase):

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
        time.sleep(3)

    def tearDown(self):
        print("测试用例结束!")

    def test_01_Regist(self):
        """ 业务逻辑, 首页-->注册--->登陆-->首页 """
        indexpage = IndexPage(self.driver)
        indexpage.go_login_regist()  
        time.sleep(3)
        # 实例化注册页面
        regist = RegistPage(self.driver)
        # u, phone, p, pwd, email
        u ="zhangsan2"
        phone="15845687954"
        p="12345678"
        pwd= "12345678"
        email="156@163.com"
        regist.Regist(u, phone, p, pwd, email)
        time.sleep(3)
        #实例化登陆页面
        loginpage = LoginPage(self.driver)
        loginpage.login(u,p)
        time.sleep(3)
        self.assertEqual(self.driver.title,indexpage.title)
