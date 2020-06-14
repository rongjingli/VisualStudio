from selenium import webdriver

driver=webdriver.Chrome(executable_path="chromedriver.exe")
# 访问shopxo前端首页
driver.get("http://132.232.44.158:9999/shopxo")
# 定位并点击MARNI Trunk 女士 中号拼色十字纹小牛皮 斜挎风琴包
driver.find_element_by_xpath('//*[@id="floor1"]/div[2]/div[2]/div[1]/div/div/a').click() 
# 定位并点击 包含斜挎风琴包连接的内容
# driver.find_element_by_partial_link_text('斜挎风琴包').click()
print(driver.title)

# 页面跳转  打印window窗口句柄
count=driver.window_handles
print("打印句柄")
print(count)
driver.switch_to_window(driver.window_handles[-1])
print(driver.title)

driver.switch_to_window(driver.window_handles[0])
print(driver.title)
# 点击首页的注册
print("结束")
driver.quit()