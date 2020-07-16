import unittest
import time
from selenium import webdriver
from utils.seleniumtools import auto_login
from utils.seleniumtools import assert_element_exist
from utils.seleniumtools import find_element
from po.UpdateuserinfoPage import UpdateuserinfoPage

from po.LoginPage import LoginPage



# 类的继承
@unittest.skip("不要想让他执行")
class TestCaseUserInfo(unittest.TestCase):
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

        login_status1 = ('link text', '登录')
        # 元素存在没有
        if assert_element_exist(self.driver, login_status1) == True:
            find_element(self.driver, login_status1).click()
            # 实例化登录页面
            loginpage = LoginPage(self.driver)
            loginpage.login("zhangsan","12345678")
        # auto_login1(self.driver)

    def tearDown(self):
        print("测试用例结束!")

    def test_01_unserinfo(self):
        usertitle = self.driver.title
        """ 点击编辑个人资料 """
        time.sleep(3)
        # 点击编辑个人资料
        self.driver.find_element_by_id('update_user_info').click()
        time.sleep(3)
        # 实例化编辑个人资料页面
        newuserinfo = UpdateuserinfoPage(self.driver)
        ximg = "D:\\toxiang.jpg"
        u = "自由的分"
        job = "软件测试1"
        sex = "男"
        phone = "18645632156"
        qq = "10374562"
        weixin = "10374562"
        email = "123@163.com"
        addr = "北京"
        userinfo = "个性签名"
        newuserinfo.Updateuser(ximg, u, job, sex, phone,
                               qq, weixin, email, addr, userinfo)
        self.assertEqual(usertitle, newuserinfo.title)
        print("个人资料结束!")
      

    


