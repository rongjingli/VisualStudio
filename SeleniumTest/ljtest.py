from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get('http://193.112.79.96:8080/ljindex/index.html')

# 点击登陆
driver.find_element_by_xpath('//*[@id="unlogin"]/div[1]/a').click() 

time.sleep(3)
# 输入用户名信息
driver.find_element_by_id('username').send_keys('zhangsan1')
driver.find_element_by_id('password').send_keys('12345678')
# 点击记住密码
# driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/ul/li[1]/label').click()
# driver.find_element_by_xpath('//*[@id="userLogin"]/font/font').click() 

driver.find_element_by_id('userLogin').click()
time.sleep(3)
# assert driver.title =="测谈网"

assert driver.current_url=="http://193.112.79.96:8080/ljindex/index.html"


print("成功了")

driver.close()
