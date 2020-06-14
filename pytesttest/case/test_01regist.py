import pytest
import requests
import os
import sys
sys.path.append(os.getcwd())
from utils.dbtools import *

# def test_reginst_01():
#     u = "http://193.112.79.96:2333/regist"
#     d = {"username": "zhangsan2", "password": "12345678","phone":"18245634561","email":"hh@163.com"}
#     res = requests.post(url=u, json=d)
#     print(res.text)
#     print(res.json()["status"])
#     assert res.status_code==200 
#     assert res.json()["status"]==200

#     # sql="select * from t_user where username='{}'".format(d.get("username"))
#     # assert len(chaxun(sql))!=0
