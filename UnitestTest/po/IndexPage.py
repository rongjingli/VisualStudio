from utils.seleniumtools import find_element

class IndexPage():
    def __init__(self,driver):
        self.driver=driver
        self.title="测谈网"
        self.url="http://193.112.79.96:8080/ljindex/index.html"
        self.loginbtn=('xpath','//*[@id="unlogin"]/div[1]/a')

    def go_login_page(self):
        """  
            进入登陆页面
       
        """
        find_element(self.driver,self.loginbtn).click()