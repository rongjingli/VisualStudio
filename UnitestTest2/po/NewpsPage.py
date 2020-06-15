from utils.seleniumtools import find_element


class NewpsPage():
    """ 设置密保页面 """

    def __init__(self, driver):
        self.driver = driver
        self.title = "找回密码"
        self.url = "http://193.112.79.96:8080/ljindex/html/update_password_logined.html?uid=undefined"
        self.password = ("id", 'oldpassword')
        self.newpassword = ("id", 'newpassword')
        self.mbbutton = ("id", 'find_password')

    def Newps(self, p,newpwd):
        """ 
        设置密保代码
        """
        find_element(self.driver, self.password).send_keys(p)   # 原有密码
        find_element(self.driver, self.newpassword).send_keys(newpwd)   # 新密码
        find_element(self.driver, self.mbbutton).click()      # 点击重置密码
