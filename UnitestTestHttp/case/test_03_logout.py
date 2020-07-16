import unittest,requests 
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import chaxun
from utils.filetools import read


@unittest.skip("屏蔽类")
class TestCaseLogout(unittest.TestCase):


    def test_01_logout(self):
        #print("hello test!")
        u ="http://49.232.185.181:2333/logout"
        token= read()
        h = {"Content-Type":"application/json","token":token}
        res= requests.get(url=u, headers=h)
        print(res.text)
        assert res.status_code ==200
        assert res.json()["status"] ==200
    
