print("hello world")
print(2333)
print(2.333)
print(None)
print(True, False)
print(())
print([])
print({})

name = "李四"
print("你好, {}".format(name))

# 单行注释
"""
多行注释
"""
num = ((3+2)*100-99)/3.2
print(num)

"""
name1 = input("请输入你的姓名: ")
print("这是input获取的值:", name1)

num1 = float(input("请输入你的第一个数: ")) 
num2 = float(input("请输入你的第二个数: "))

num3 = num1+num2
print(num3)

name2 = input("请输入: ")
name3 = len(name2)
print(name3)
"""

# 元组
a = ("哈哈哈", "希希", "黑盒", "黑盒", "黑盒", 123, True, False, None, 1, 0, 1)
print(a)
print(a[3])
print(a.index("黑盒"))
print(a.count(True))
# 数组
b = ["哈哈哈", "希希", "黑盒", "黑盒", "黑盒", 123, True, False, None, 1, 0, 1]
print(b)
print(b[3])
print(b.index("黑盒"))
print(b.count(True))
b.append("星期天")
print(b)
b.insert(1,"你好")
print(b)

c=[2,5,4,65,13,88,46,95,23,7]
""" 
c.sort  #排序
c.reverse #颠倒
c.sort(reverse=True) #倒序 


x = b.pop(0) #取出
print(x)
print(b)

b.remove("黑盒") #删除
print(b)
b.clear  #清空
print(b)
b.extend(4,5,3)  #追加,合并数组
print(b)
"""
d =[a,b]
print(d[1][1])

e =(b,0)
print(e)
e[0].append("昕昕")
e[0].insert(1,"兰兰")
print(e)
