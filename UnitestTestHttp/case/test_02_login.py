import unittest,requests 
import os, sys
sys.path.append(os.getcwd())
from utils.filetools import save
from utils.dbtools import chaxun
from utils.geturlParams import geturlParams


@unittest.skip("屏蔽类")
class TestCaseLogin(unittest.TestCase):

    def setUp(self):
        # geturlParams().get_Url()
        self.base_url = geturlParams().get_Url() + "/login"

    def tearDown(self):
        print(self.result)

    def test_01_login(self):
        #print("hello test!")
        d = {"username":"zhangsan2", "password":"12345678"}
        res = requests.post(self.base_url, json=d)
        self.result = res.json()
        print(res.text)
        assert res.status_code ==200
        # assert res.json()["status"] ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '登录成功！')
        token=self.result["data"]["token"]

        sql ="select * from t_user where username ='{}'".format(d.get("username"))
        assert len(chaxun(sql))!= 0
        save(res)