from dbtools import *

# 登陆
userid =int(input("请输入账号id:"))
username = input("请输入账号:")
password = input("请输入密码:")

# sql ='select * FROM user where Username ="{}" and Password ="{}"'.format(username,password)
def sename(userid):
    #sql ='select * FROM user where Username ="{}" and Password ="{}"'.format(username,password)
    sql ='select * FROM user where id ={}'.format(userid)

    res = chaxun(sql)
    if len(res)!=0:
        print("查询成功!")
        print(res)
    else:
        print("查询失败!")
    pass
#sename(userid)

cr_sql="insert into user values({},'{}','{}')".format(userid,username,password)
res =commit(cr_sql)
if res == True:
    sename(userid)
    print("注册成功!")
    pass
else:
    print("注册失败!")
    pass

