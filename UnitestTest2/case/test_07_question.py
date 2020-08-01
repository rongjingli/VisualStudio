import unittest
import time
from selenium import webdriver
from utils.seleniumtools import assert_element_exist
from utils.seleniumtools import auto_login
from po.QuestionPage import QuestionPage

# 类的继承
# @unittest.skip("不要想让他执行")
class TestCaseQuestion(unittest.TestCase):
    """ 修改密码 """

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
        # 调用判断自动登陆
        auto_login(self.driver)
        time.sleep(3)
        
      
        time.sleep(3)
    def tearDown(self):
        print("测试用例结束!")


    def test_01_question(self):
        """用户提问页面 """
        self.driver.find_element_by_xpath('html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[3]').click()
        time.sleep(3)
        usertitle = self.driver.title   
        questionPage = QuestionPage(self.driver)
        title="如何成为优秀的测试工程师"
        content="如何成为优秀的测试工程师呢" 
        ximg = "D:\\toxiang.jpg"
        brief="职业指南"  #简介
        new_tag="测试工程师"  
        questionPage.question(title, content, ximg, brief, new_tag)

        
        self.assertEqual(usertitle, questionPage.title)
        print("用户添加提问结束!")



