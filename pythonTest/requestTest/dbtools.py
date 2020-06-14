import pymysql

def chaxun(sql):
    db =pymysql.connect(host="193.112.79.96",user="root",password="123456",db="jiradb")
    cur=db.cursor()
    cur.execute(sql)
    # 得到执行的结果
    res = cur.fetchall()
    db.close()
    return res

def commit(sql):
    db =pymysql.connect(host="193.112.79.96",user="root",password="123456",db="jiradb")

    cur=db.cursor()
    cur.execute(sql)
    # 提交修改
    db.commit()
    db.close()
    return True
    pass

""" sql="select * from user"
res =chaxun(sql)
if len(res)!=0:
    print("查询成功")
    print(res)
    pass
else:
    pass
 """


#sql="insert into user values(3,'jlj','123')"

# sql ='update user set Username = "你好呀" WHERE id =3'
#删除user表第三条
""" sql ='DELETE  from user where id =5'

res1 =commit(sql)
if res1==True:
    print("成功")
    print(res1)
    pass
else:
    print("失败")
    pass 
 """


