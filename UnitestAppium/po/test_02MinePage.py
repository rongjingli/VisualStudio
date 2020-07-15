from utils.appiumtools import find_element


class MinePage():

    def __init__(self, driver):
        """ 我的页面元素 """
        self.driver = driver
        self.title = "登录"
        self.username = "158****0856"
        # 请登陆/用户名/编辑
        self.user_nickname = ("id", 'com.znb.zxx:id/user_nickname_view')
        # 待支付
        self.un_pay = ("id", 'com.znb.zxx:id/un_pay_part_view')
        self.un_send = ("id", 'com.znb.zxx:id/un_send_part_view')  #代发货
        self.un_receive = ("id", 'com.znb.zxx:id/un_receive_part_view') #待收货
        self.all_order = ("id", 'com.znb.zxx:id/all_order_part_view') #全部订单
        
        self.follow_part = ("id", 'com.znb.zxx:id/follow_part_view') #我的关注
        self.class_part = ("id", 'com.znb.zxx:id/class_part_view') #我的课程
        self.collect_part = ("id", 'com.znb.zxx:id/collect_part_view') #我的收藏
        self.ebook_part = ("id", 'com.znb.zxx:id/ebook_part_view') #我的电子书
        self.resume_part = ("id", 'com.znb.zxx:id/resume_part_view') #我的简历
        self.paper_part = ("id", 'com.znb.zxx:id/paper_part_view') #我的真题
        self.setting_part = ("id", 'com.znb.zxx:id/setting_part_view') #设置



    def login(self):
        """ 
        进入请登陆页面/编辑账号中心
        """
        find_element(self.driver, self.user_nickname).click()
