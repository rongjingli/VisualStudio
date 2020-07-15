from utils.appiumtools import find_element


class LoginPage():

    def __init__(self, driver):
        """ 登陆页面元素 """
        self.driver = driver
        self.title = "登录"

        # 验证码登录
        self.YZlogin=('text','验证码登录') 
        # 密码登录
        self.pwdlogin=('text','密码登录') 
        self.phone = ("id", 'com.znb.zxx:id/phone_edit_view')  # 手机号
        self.pwd = ("id", 'com.znb.zxx:id/pwd_edit_view')  # 密码
        self.confirm = ("id", 'com.znb.zxx:id/confirm_view')   #登录/获取验证码
        self.agreement = ("id", 'com.znb.zxx:id/_view')  #协议

        self.regist = ("id", 'com.znb.zxx:id/regist_view')  #新用户注册
        self.agreement = ("id", 'com.znb.zxx:id/forget_pwd_view')  #忘记密码
        #编辑个人信息
        self.information = ("xpath", '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]')



    def y_login(self, u):
        """ 
        验证码登陆
        """
        find_element(self.driver, self.YZlogin).click()
        find_element(self.driver, self.phone).send_keys(u)
        find_element(self.driver, self.confirm).click()

    def Pwdlogin(self, u, p):
        """ 
        验证码登陆
        """
        find_element(self.driver, self.pwdlogin).click()
        find_element(self.driver, self.phone).send_keys(u)
        find_element(self.driver, self.pwd).send_keys(p)
        #协议
        find_element(self.driver, self.agreement).click()  
        find_element(self.driver, self.confirm).click()


    def go_regist(self, u, p):
        """ 
        进入注册页面
        """ 
        find_element(self.driver, self.regist).click()

    def go_agreement(self, u, p):
        """ 
        进入忘记密码页面
        """
        find_element(self.driver, self.agreement).click()

    def go_information(self):
        """ 
        进入编辑账号中心页面information
        """
        find_element(self.driver, self.information).click()
        
