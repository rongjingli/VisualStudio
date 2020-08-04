import pytest
import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import chaxun
from utils.filetools import save

# def test_01_login():
#     #print("hello test!")
#     u = "http://49.232.185.181:2333/login"
#     d = {"username":"zhangsan2", "password":"12345678"}
#     res = requests.post(url=u,json=d)
#     print(res.text)
#     assert res.status_code ==200
#     assert res.json()["status"] ==200
#     token=res.json()["data"]["token"]

#     sql ="select * from t_user where username ='{}'".format(d.get("username"))
#     assert len(chaxun(sql))!= 0
#     save(res)
    


   