from utils.seleniumtools import find_element
import time


class UpdateuserinfoPage():
    """ 修改个人资料页面 """

    def __init__(self, driver):
        self.driver = driver
        self.title = "测评网-个人信息"
        # self.url = "http://193.112.79.96:8080/ljindex/html/personal_info.html?uid="+uid
        self.ximg = ("name", 'file')
        self.nickname = ("id", 'username')
        self.phone = ("id", 'phone')
        self.sex = ("id", 'sex')
        self.job = ("id", 'job')
        self.email = ("id", 'modify-mailbox')
        self.weixin = ("id", 'weixin')
        self.qq = ("id", 'qq')
        self.address = ("id", 'addr')
        self.userinfo = ("id", 'qianming')
        self.acommit1 = ("id", 'acommit1')

    def Updateuser(self, ximg,u, job, sex, phone, qq, weixin, email,address,userinfo):
        """ 
        提交个人资料代码
        """
        find_element(self.driver, self.ximg).send_keys(ximg)   # 头像
        time.sleep(3)
        # self.driver.switch_to_alert()
        dig_alert = self.driver.switch_to_alert()
        assert dig_alert.text =="修改成功！"
        self.driver.switch_to_alert().accept()
        time.sleep(3)
        find_element(self.driver, self.nickname).clear()   # 清空昵称
        find_element(self.driver, self.nickname).send_keys(u)   # 输入昵称
        find_element(self.driver, self.job).clear()   # 清空职业
        find_element(self.driver, self.job).send_keys(job)   # 职业
        find_element(self.driver, self.sex).clear()   # 清空性别
        find_element(self.driver, self.sex).send_keys(sex)   # 性别
        find_element(self.driver, self.phone).clear()   # 清空电话
        find_element(self.driver, self.phone).send_keys(phone)   # 电话
        find_element(self.driver, self.qq).clear()   # 清空qq号
        find_element(self.driver, self.qq).send_keys(qq)   # qq号
        find_element(self.driver, self.weixin).clear()   # 清空微信号
        find_element(self.driver, self.weixin).send_keys(weixin)   # 微信号
        find_element(self.driver, self.email).clear()           #清空邮箱 
        find_element(self.driver, self.email).send_keys(email)   # 邮箱 
        find_element(self.driver, self.address).clear()   # 清空地址
        find_element(self.driver, self.address).send_keys(address)   # 地址
        find_element(self.driver, self.userinfo).clear()   # 清空个性签名
        find_element(self.driver, self.userinfo).send_keys(userinfo)   # 个性签名
        find_element(self.driver, self.acommit1).click()      # 点击修改
