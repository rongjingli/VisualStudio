import unittest, time
from selenium import webdriver
from utils.seleniumtools import auto_login
from utils.seleniumtools import find_element
from utils.seleniumtools import assert_element_exist
from po.IndexPage import IndexPage
from po.LoginPage import LoginPage

class TestCaseQuestion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver\chromedriver.exe')
        cls.driver.maximize_window()

    # 在类结束的时候运行
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

     # test_开始执行的时候执行
    def setUp(self):
        self.driver.get('http://193.112.79.96:8080/ljindex/index.html')
        #auto_login(self.driver) 这两个一样
        login_status = ('link text', '登录')
        # 元素存在没有
        if assert_element_exist(self.driver, login_status) == True:
            indexpage = IndexPage(self.driver)
            indexpage.go_login_page()
            time.sleep(3)
            # 实例化登录页面
            loginpage = LoginPage(self.driver)
            loginpage.login("zhangsan","12345678")
            

    def test_01_tiwen(self):
        # 首先要登录
       
        # 这是一个问题,定位并点击进去
        q1 = ("xpath", '//*[@id="questsions"]/li/p')
        find_element(self.driver, q1).click()
        
        time.sleep(3)
       
        plk = ("id", 'question_comments_ctt')  
        plan = ("id", 'question_comments_btn')
        # 定位评论框 并输入内容
        find_element(self.driver, plk).send_keys("来自动化测试的评论！")
        time.sleep(3)
        # 点击评论按钮
        find_element(self.driver, plan).click()
        time.sleep(3)