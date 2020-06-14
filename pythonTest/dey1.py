import test.a


# 变量
db = [{"username": "chenke", "password": "123456"},{"username": "哥哥", "password": "123456"}]
# 输入
u = input("请输入账号：")
p = input("请输入密码：")

count =1
for i in db:
    if u==i.get("username"):
        i["password"] ="13321"
        break
    else:
        if len(db)==count:
             db.append({"username": u, "password": p})
    print(count) 
    count = count+1
print(db)