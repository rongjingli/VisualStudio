from utils.seleniumtools import find_element


class MbPage():
    """ 设置密保页面 """

    def __init__(self, driver):
        self.driver = driver
        self.title = "添加密码保护"
        self.url = "http://193.112.79.96:8080/ljindex/html/set_mb.html"
        self.password = ("id", 'password')
        self.q1 = ("id", 'q1')
        self.a1 = ("id", 'a1')
        self.q2 = ("id", 'q2')
        self.a2 = ("id", 'a2')
        self.q3 = ("id", 'q3')
        self.a3 = ("id", 'a3')
        self.mbbutton = ("id", 'set_mb_question')

    def Mbuser(self, p,q1, a1,q2,a2,q3,a3):
        """ 
        提交个人资料代码
        """
        find_element(self.driver, self.password).send_keys(p)   # 原有密码
        find_element(self.driver, self.q1).send_keys(q1)        # 问题1
        find_element(self.driver, self.a1).send_keys(a1)        # 答案1
        find_element(self.driver, self.q2).send_keys(q2)        # 问题2
        find_element(self.driver, self.a2).send_keys(a2)        # 答案2
        find_element(self.driver, self.q3).send_keys(q3)        # 问题3
        find_element(self.driver, self.a3).send_keys(a3)        # 答案3
        find_element(self.driver, self.mbbutton).click()      # 点击修改
