from selenium import webdriver
import unittest, time,requests
from utils.dbtools import chaxun
from utils.filetools import save
from utils.filetools import read

# @unittest.skip("屏蔽类")
class TestCaseLogin(unittest.TestCase):

    def setUp(self):
        print("接口测试开始")
        self.URL="http://193.112.79.96:2333"
    def tearDown(self):
        print("接口测试结束!")

    def test_01_login(self):
        """
            这是登录方法
        """
        url = self.URL+"/login"
        data = {"username":"zhangsan", "password":"12345678"}
        res = requests.post(url=url , json=data)
        assert res.status_code == 200 and res.json()["status"] == 200
        
        
        sql = "select * from t_user where username = '{}'".format(data.get("username"))
        assert len(chaxun(sql)) != 0

        # 保存token,不保存token
        save(res)

    def test_02_logout(self):
        """
            这是用户退出的方法
        """
        token = read()
        url = self.URL+"/logout"
        header = {"Content-Type":"application/json","token":token}
        res = requests.get(url=url, headers=header)
        assert res.status_code == 200 and res.json()["status"] == 200