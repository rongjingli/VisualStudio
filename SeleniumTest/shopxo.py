from selenium import webdriver
import time

# shopxo后台
driver = webdriver.Chrome(executable_path="chromedriver.exe")
# 访问登陆页面
driver.get('http://132.232.44.158:9999/shopxo/admin.php')
# 输入用户名信息
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[1]/input').send_keys('admin')
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[2]/input').send_keys('shopxo')
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()
time.sleep(3)
# 跳转后定位首页
driver.find_elements_by_xpath('//*[@id="admin-offcanvas"]/div/ul/li[1]/a/span[2]')
print(driver.title)
time.sleep(3)
# iframe 是嵌套网页
iframe =driver.find_element_by_id("ifcontent")
driver.switch_to_frame(iframe)

usercount= driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[1]/div/p[2]')
print(usercount.text)
# 退出iframe i扶瑞姆
driver.switch_to_default_content()
time.sleep(3)
# 首页的系统设置定位
driver.find_element_by_xpath('//*[@id="admin-offcanvas"]/div/ul/li[2]/a/span[2]')

driver.quit()