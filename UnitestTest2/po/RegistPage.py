from utils.seleniumtools import find_element
import time


class RegistPage():
    """ 注册页面 """

    def __init__(self, driver):
        self.driver = driver
        self.title = "注册"
        self.url = "http://193.112.79.96:8080/ljindex/html/register.html"
        self.username = ("id", 'username')
        self.phonenum = ("id", 'phonenum')
        self.password = ("id", 'password')
        self.confirpw = ("id", 'confirpw')
        self.emailnum = ("id", 'emailnum')
        self.userRegist = ("id", 'userRegist')
        # self.dig_alert = driver.switch_to_alert()
        # self.dig_accept = driver.switch_to_alert().accept()

    def Regist(self, u, phone, p, pwd, email):
        """ 
        注册代码
        """
        find_element(self.driver, self.username).send_keys(u)       # 用户名
        find_element(self.driver, self.phonenum).send_keys(phone)   # 电话
        find_element(self.driver, self.password).send_keys(p)       # 密码
        find_element(self.driver, self.confirpw).send_keys(pwd)     # 重复密码
        find_element(self.driver, self.emailnum).send_keys(email)   # 邮箱地址
        find_element(self.driver, self.userRegist).click()          # 点击注册
        time.sleep(5)
        # 进入alert弹窗提醒页面
        self.driver.switch_to_alert()
        # 点击alert确定按钮
        self.driver.switch_to_alert().accept()

