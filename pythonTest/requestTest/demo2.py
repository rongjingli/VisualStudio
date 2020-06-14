import requests
from dbtools import *


#登陆
url ="http://193.112.79.96/:2333/login"
parameter ={"username":"wanghao123","password":"123456789"}
res = requests.post(url =url, json=parameter)
print(res.text)
#token =res.json()["data"]["token"]
#判断结果,http状态码/结果码
#断言

assert res.status_code == 200  
assert res.json()["status"] == 200 # 完成结果码的判断



# 查询数据库
sql="select * from user where username={}".format(parameter.get("username"))
res =chaxun(sql)
if len(res)!=0:
    print("接口测试成功")
    print(res)
    
else:
    print("接口测试失败!")
