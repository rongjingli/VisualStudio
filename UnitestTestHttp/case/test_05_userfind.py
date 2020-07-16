import unittest,requests 
import os, sys
sys.path.append(os.getcwd())
from utils.filetools import save
from utils.filetools import read
from utils.dbtools import chaxun
from utils.geturlParams import geturlParams


# @unittest.skip("屏蔽类")
class TestCaseLogin(unittest.TestCase):

    def setUp(self):
        # geturlParams().get_Url()
        self.base_url = geturlParams().get_Url()

    def tearDown(self):
        print(self.result)

    # @unittest.skip("skipping") # 无条件忽略该测试方法
    def test_01_serfindps(self):
        """ 找回密码/设置新密码 """
        d = {"username":"zhangsan2", "password":"12345678",
             "mb":{ 
                 "1":"答案", 
                 "2":"答案", 
                 "3":"答案" 
                 }
            }
        res = requests.post(self.base_url+"/userfindps", json=d)
        self.result = res.json()
        print(res.text)
        assert res.status_code ==200
        # assert res.json()["status"] ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '设置密码成功！')


    def test_02_regist(self):
        """ 用户注册接口 """
        d = {
             "username":"zhangsan3",    #账号
             "password":"12345678",     #密码
             "phone":"18212341234",     #电话
             "email":"hhh@163.com"      #邮箱
            }
        res = requests.post(self.base_url+"/regist", json=d)
        self.result = res.json()
        print(res.text)
        assert res.status_code ==200
        # assert res.json()["status"] ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], 'true,')

    def test_03_login(self):
        """ 用户注册接口 """
        d = {
             "username":"zhangsan3",    #账号
             "password":"12345678",     #密码
            }
        res = requests.post(self.base_url + "/login", json=d)
        self.result = res.json()
        print(res.text)
        assert res.status_code ==200
        # assert res.json()["status"] ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], 'true,')


  

    def test_04_logout(self):
        """ 退出登陆 """

            token= read()
            h = {"Content-Type":"application/json","token":token}
            res= requests.get(url=self.base_url+"/logout", headers=h)
            self.result = res.json()
            print(res.text)
            self.assertEqual(self.result['status'], 200)
            self.assertEqual(self.result['msg'], '登录成功！')  