from utils.seleniumtools import find_element

class GetinspirerPage():
    """     
       灵感页面
    """
    def __init__(self, driver):
        self.driver = driver
        self.title = "测评网-写文章"
        self.url = "http://193.112.79.96:8080/ljindex/html/experience_new.html"
        self.content = ("id", 'message')
        self.icon=("class name",'icon')
        self.ximg = ("name", 'file')
        self.getinspirercommit = ("id", 'commit')


    def question(self,  content, icon, ximg):
        """ 
        添加;灵感代码
        """
        find_element(self.driver, self.content).send_keys(content)  # 内容
        find_element(self.driver, self.icon).send_keys(icon)      # 标签
        find_element(self.driver, self.ximg).send_keys(ximg)        # 图片
        find_element(self.driver, self.getinspirercommit).click()      # 点击问题提交
