from utils.seleniumtools import find_element


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.title = "登录"
        self.url = "http://193.112.79.96:8080/ljindex/html/login.html"
        self.username = ("id", 'username')
        self.password = ("id", 'password')
        self.userLogin = ("id", 'userLogin')

    def login(self, u, p):
        """ 
        登陆代码
        """
        find_element(self.driver, self.username).send_keys(u)
        find_element(self.driver, self.password).send_keys(p)
        find_element(self.driver, self.userLogin).click()
