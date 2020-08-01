from selenium import webdriver
import time, unittest
from utils.seleniumtools import assert_element_exist

# 类的继承
# @unittest.skip("不")
class TestCassindex(unittest.TestCase):
    # 类开始运行前运行一次
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        # cls.driver.maximize_window()
    # 类结束运行前运行一次
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 在test_测试方法开始之前执行
    def setUp(self):
        print("测试用例开始!")
        self.driver.get("http://49.232.185.181:8080/ljindex/index.html")
    
    # 在test_测试方法结束之前执行
    def tearDown(self):
        print("测试用例结束了")

    # 成员方法: 类里面的方法: self
    def test_01_coure(self):
        jc = ( "xpath", '/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/button')
        assert assert_element_exist(self.driver, jc)==True

    
    # 测试主页定位问题模块
    def test_02_question(self):
        # 这是一个问题
        jc=("xpath",'/html/body/div[2]/div[2]/div/div[1]/div[2]/div[1]/div')
        assert assert_element_exist(self.driver, jc)==True
    # 定位活跃用户模块
    def test_03_article(self):
        # 用户1952992
        jc = ("xpath", '/html/body/div[2]/div[2]/div/div[1]/div[5]/div[1]')
        assert assert_element_exist(self.driver, jc) == True
  

if __name__ == "__main__":
    unittest.main()
