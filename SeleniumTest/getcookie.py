from selenium import webdriver
import time
from filetools import *

driver=webdriver.Chrome(executable_path="chromedriver.exe")
# 访问shopxo前端首页
driver.get("http://132.232.44.158:9999/shopxo")
# 点击登陆
driver.find_element_by_xpath('/html/body/div[2]/div/ul[1]/div/div/a[1]').click()
# 输入账号
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[1]/input').send_keys('admin1')
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[2]/input').send_keys('123456')
time.sleep(10)
# 验证码手动输入
# driver.find_element_by_xpath().send_keys()

# 点击登陆按钮 
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[4]/button').click()
# 获取cookie
# cookie=  driver.get_cookies()

# print(cookie)
# 保存到cookie.txt中
save(driver)

# 读出cookie并打印
print(read())


time.sleep(4)
# 退出登陆 
# driver.find_element_by_xpath('/html/body/div[2]/div/ul[1]/div/div/a').click()

driver.quit()