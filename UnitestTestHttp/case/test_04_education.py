import unittest,requests 
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import chaxun
from utils.filetools import read


@unittest.skip("屏蔽类")
class TestCaseEducationt(unittest.TestCase):


    def test_01_education(self):
        #print("hello test!")
        u ="http://beta.tobebetterman.com/education/add-eplan"
        p={'token': 'e1b98e4317985f341de3f491ba8683d115943595'}
        payload = {"plans": 
                    [
                        ['17:00'], 
                        ['18:00'], 
                        ['数学辅导课'],
                        [ 1]
                    ]
                  }
    #    params=p,
        res= requests.post(url=u, params=p, data=payload)
        print(res.text)
        assert res.status_code ==200
        assert res.json()["code"] ==200
        assert res.json()["result"] =="添加成功"
    
