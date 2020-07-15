from utils.appiumtools import find_element


class InformationPage():

    def __init__(self, driver):
        """ 账号中心 """
        self.driver = driver
        self.title = "登录"
        self.username = "158****0856"
        # 头像
        self.icon_part_view = ("id", 'com.znb.zxx:id/icon_part_view')
        #拍照
        self.edia_camera = ("id", 'com.znb.zxx:id/dialog_system_edia_camera')
        #从相册中选
        self.edia_album = ("id", 'com.znb.zxx:id/dialog_system_edia_album')
        #始终允许
        self.permission = ("id", 'com.android.permissioncontroller:id/permission_allow_button')
        self.camera = ("text", '相机') #定位相机里的照片
        #定位第一张照片
        self.camera = ("xpath", '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout')
        
        #取消
        self.edia_cancle = ("id", 'com.znb.zxx:id/dialog_system_edia_cancle')
        #昵称
        self.nickname = ("id", 'com.znb.zxx:id/nickname_view')
        #昵称输入框
        self.nickname_settext = ("id", '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView')
        #完成1
        self.complete = ("id", 'com.znb.zxx:id/base_toolbar_extra_text') 


        self.sex_setText = ("id", 'com.znb.zxx:id/gender_view')  # 性别
        self.man = ("text", '男')  # 性别
        self.girl = ("text", '女')  # 性别
        self.cancel = ("text", '取消')  # 性别
        self.ok = ("text", '完成')  # 性别


        self.birthday = ("id", 'com.znb.zxx:id/birthday_view')  #生日
        self.location = ("id", 'com.znb.zxx:id/location_view') #所在地区
        self.mail = ("id", 'com.znb.zxx:id/mail_view') #邮箱
        #邮箱输入框
        self.mail_settext = ("id", '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView') #邮箱
        #完成1=一样的


    def update_img(self):
        """ 
        修改头像操作
        """
        find_element(self.driver, self.icon_part_view).click()
        find_element(self.driver, self.edia_album).click()
        find_element(self.driver, self.permission).click()   #访问摄像投权限
        find_element(self.driver, self.camera).click()   #访问相机分类里的相片



