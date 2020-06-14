""" age = int(input("请输入年龄:"))
if age>18:
    print("成年人")
else:
    print("未成年人")

c = "快乐儿童节"
b = "儿童"
if b in c:
    print("b在c中找到")
else:
    print("不在")

a = [1, 2, 3, 8, 5, 7, 9]
a.sort
print(a)
a.append(10)
print(a)
 for  i in a:
    print(i)

作业
task = {"autograph": "每天更好", "地址": "不是真的"}

name = input("请输入name:")
age = int(input("请输入age:"))
sex = input("请输入sex:")

task["name"]=name
task["age"]=age
task["sex"]=sex

print(task)
"""
# 作业：输入账号和密码，去判断db中是否存在该账号，如果已存在，就修改该账号的密码，如果不存在，就再添加一个字典
# db  = [{ “ username”：“ chenke”，“ password”：“ 123456” }]
# 输入一个账号为chenke，那就需要把密码改成输入的密码
# 输入的账号是zqc，那就添加一个字典
# db = [{“ username”：“ chenke”，“ password”：“ 123456”}，{“ username”：“ zqc”，“ password”：“ 123456”}]

# 变量
db = [{"username": "chenke", "password": "123456"}]
# 输入
u = input("请输入账号：")
p = input("请输入密码：")

# 循环判断db中有没有账号zqc的账号
for i in db:
    # 如果有：就去修改zqc的账号
    if u == i.get("name"):
        i["name"] = "哈哈"
        print("修改并打印:")
        print(i)
        break
    else:
        """ 
        # 如果没有：就要去添加zqc的账号和密码
        i["name"] = u
        i["pwd"] = p
        print("添加并打印")
        print(i)
       
       就要去添加zqc的账号和密码 {"username": "zqc", "password": "123456"}
       c ={}
        c["username"] = "zqc"
        c["password"] = "123456"
        db.append(c) 
        """
        db.append({"username": "zqc", "password": "123456"})
print(db)
