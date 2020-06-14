from selenium import webdriver
import time, unittest
from utils.seleniumtools import *
# 显示等待必须加这个
# from selenium.webdriver.support.ui import WebDriverWait

# 类的继承
@unittest.skip("不要想让他执行")
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
        self.driver.get("http://193.112.79.96:8080/ljindex/index.html")
    
    # 在test_测试方法结束之前执行
    def tearDown(self):
        print("测试用例结束了")

    # 成员方法: 类里面的方法: self
    def test_01_coure(self):
        # self.driver.get("http://193.112.79.96:8080/ljindex/index.html")
        # time.sleep(3) 强制等待
        # driver.implicitly_wait(10) 等待网页加载后再去执行,隐士等待最多等10秒.不到10秒找到,是直接执行,多余的秒自动忽略
        # 调用方法,显示等待,元素
        jc = ( "xpath", '/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/button')
        # e = find_element(self.driver, jc).text
        # e= driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/button').text
        # assert e == "查看教程"
        # self.assertEqual(e,"查看教程") unittest自带的断言
        # 调用assert_element_exist方法断言元素有没有找到
        assert assert_element_exist(self.driver, jc)==True

    
    # 测试主页定位问题模块
    def test_02_question(self):
        # 这是一个问题
        jc=("xpath",'//*[@id="questsions"]/li/p')
        assert assert_element_exist(self.driver, jc)==True
    # 定位活跃用户模块
    def test_03_article(self):
        # 用户1952992
        jc = ("xpath", '//*[@id="hotuser"]/li[1]/span')
        assert assert_element_exist(self.driver, jc) == True
    # test_02_assert=assert_element_exist一个意思,判断元素有没有,有就是true,没False
    # def test_02_assert(self):
    #     a =True
    #     # self.assertTrue (a)
    #     self.assertFalse (a)


if __name__ == "__main__":
    unittest.main()
