import pytest
import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import chaxun
from utils.filetools import read



# def test_02_logout():
    
#     u ="http://49.232.185.181:2333/logout"
#     token= read()
#     h = {"Content-Type":"application/json","token":token}
#     res= requests.get(url=u, headers=h)
#     print(res.text)
#     assert res.status_code ==200
#     assert res.json()["status"] ==200
