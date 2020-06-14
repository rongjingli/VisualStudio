# 导入selenium
from selenium import webdriver

# 打开chrome浏览器,实例化句柄  executable_path 英 [ɪɡˈzekjətəbl] 一刻ri可不   英 [pɑːθ]怕死
driver = webdriver.Chrome(executable_path='chromedriver.exe')
# Chrome英 [krəʊm]

# 访问百度
driver.get("https://www.baidu.com/")

# driver.maximize_window()  窗口最大化
# 输入内容并点击搜索
# driver.find_element_by_id('kw').send_keys("selenium好简单")
# driver.find_element_by_id('su').click()  #点击
a= driver.title #调用属性,获取标题
print(a)

b= driver.current_url  #获取url
print(b)



e= driver.find_element_by_xpath(".//*[@id='kw']")
e.test()
