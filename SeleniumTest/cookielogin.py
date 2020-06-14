from selenium import webdriver
import time
from filetools import *


def get_page(url):
    driver=webdriver.Chrome(executable_path="chromedriver.exe")
    # 访问shopxo前端首页
    driver.get(url)
    # driver.get("http://132.232.44.158:9999/shopxo")
    # 删除之前的cookies信息
    driver.delete_all_cookies() 

    cookies ={'domain': '132.232.44.158', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'd3gpus5q02a3lqkn1trkelfr90'}
    # 从read()方法中读取cookie并赋值
    # cookies = read()

    driver.add_cookie(cookies)
    # 刷新页面
    driver.refresh()
    time.sleep(3)
    # driver.quit()
    return driver

driver = get_page("http://132.232.44.158:9999/shopxo/")
