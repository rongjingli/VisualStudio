import unittest,time
from selenium import webdriver
from po.IndexPage import IndexPage
from po.LoginPage import LoginPage
from po.UpdateuserinfoPage import UpdateuserinfoPage
from utils.seleniumtools import auto_login1
# 类的继承
# @unittest.skip("不要想让他执行")
class TestCaseUserInfo(unittest.TestCase):
    """ 个人信息页面 """

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
        # 调用判断自动登陆
        auto_login1(self.driver)

    def tearDown(self):
        print("测试用例结束!")

    def test_01_unserinfo(self):
        """ 业务逻辑, 首页--->登陆-->个人信息 """
        # 主页点击用户头像跳转个人信息页面
        self.driver.find_element_by_id('headpic_nav').click()
        usertitle= self.driver.title
        time.sleep(3)
        # 点击编辑个人资料
        self.driver.find_element_by_id('update_user_info').click()
        time.sleep(3)
        # 实例化编辑个人资料页面
        newuserinfo = UpdateuserinfoPage(self.driver)
        ximg="C:\\Users\\Administrator\\Pictures\\9fa098145c6ccb60a4364f72517f1312.jpg"
        u="自由的分"
        job="软件测试" 
        sex="男"
        phone="18645632156"
        qq="10374562"
        weixin="10374562"
        email="123.163.com"
        addr="北京"
        userinfo="个性签名"
        newuserinfo.Updateuser(ximg, u, job, sex, phone, qq, weixin, email, addr, userinfo)
        self.assertEqual(usertitle,"测谈网-个人信息")



