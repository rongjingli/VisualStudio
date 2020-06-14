from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get('http://193.112.79.96:8080/ljindex/index.html')

# 点击注册
driver.find_element_by_xpath(".//*[@id='unlogin']/div[2]/a").click() 

time.sleep(3)
# 输入用户名信息
driver.find_element_by_id('username').send_keys('zhangsan3')
# 手机号
driver.find_element_by_id('phonenum').send_keys('15834569452')
# 密码
driver.find_element_by_id('password').send_keys('12345678')
# 重复密码
driver.find_element_by_id('confirpw').send_keys('12345678')
# 邮箱
driver.find_element_by_id('emailnum').send_keys('123@163.com')
# 注册
driver.find_element_by_xpath(".//*[@id='userRegist']").click()
time.sleep(3)
# assert driver.title =="测谈网"

# 获取alert对话框 alert e额乐特
dig_alert = driver.switch_to_alert()
time.sleep(1)
# 打印警告对话框内容
# assert dig_alert.text =="用户名已存在，请重新设置！"
# 验证用户名已存在 在警告对话框内容中
assert "用户名已存在" in dig_alert
print(dig_alert.text)

# driver.switch_to.alert().accept #点击弹窗确定accept饿可塞普特
driver.switch_to_alert.accept()
#driver.switch_to_alert.dismiss()#点击弹窗取消
# alert对话框属于警告对话框，我们这里只能接受弹窗

time.sleep(1)

#assert driver.current_url=="http://193.112.79.96:8080/ljindex/index.html"
#print("成功了")

#driver.close()
driver.quit()