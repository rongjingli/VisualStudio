import pymysql
# import readConfig
from utils.readConfig import ReadConfig

readConfig = ReadConfig()
host = readConfig.get_mysql('host')
user = readConfig.get_mysql('user')
password = readConfig.get_mysql('password')
db2 = readConfig.get_mysql('db')

# class DBtools():
def chaxun(sql):
        # db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
        db =pymysql.connect(host = host,user = user,password = password,db = db2)
        cur=db.cursor()
        cur.execute(sql)
        # 得到执行的结果
        res = cur.fetchall()
        db.close()
        return res

def commit(sql):
        db =pymysql.connect(host = host,user = user,password = password,db = db2)
        # db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
        cur=db.cursor()
        cur.execute(sql)
        # 提交修改
        db.commit()
        db.close()
        return True

if __name__ == '__main__':

    sql="select * from user"
    res =chaxun(sql)
    if len(res)!=0:
        print("查询成功")
        print(res)
        pass
    else:
        pass