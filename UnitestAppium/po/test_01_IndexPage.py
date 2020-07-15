from utils.appiumtools import find_element

class IndexPage():
    def __init__(self,driver):
        """ 首页元素 """
        self.driver=driver
        self.select=('id','com.znb.zxx:id/home_search_view')  #查找
        #职业规划
        self.career_planning=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.ImageView')  
        #资格证书
        self.qualification=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.ImageView')  
        #考公考编
        self.examination=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[3]/android.widget.ImageView')  
        #升学考试
        self.Entrance_examination=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[4]/android.widget.ImageView')  
        #求职创业
        self.Entrepreneurship=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout[5]/android.widget.ImageView') 
        #我的生涯
        self.select=('text','职业目标') 
        self.select=('text','升学目标') 
        self.select=('text','考编目标') 
        # 首页
        self.wode=('id','com.znb.zxx:id/navigator_mine_view')
        #课程
        self.class_view=('id','com.znb.zxx:id/navigator_class_view')
        #图书
        self.book_view=('id','com.znb.zxx:id/navigator_book_view')
        
        #我的
        self.mine_view=('id','com.znb.zxx:id/navigator_mine_view')


    def go_mine_view(self):
        """  
            进入个人主页
        """
        find_element(self.driver,self.mine_view).click()
        
    def go_book_page(self):
        """  
            进入图书页面
        """
        find_element(self.driver,self.book_view).click()

    def go_class_page(self):
        """  
            进入课程页面
        """
        find_element(self.driver,self.class_view).click()

    def go_career_planning(self):
        """  
            进入职业规划页面
        """
        find_element(self.driver,self.career_planning).click()

    def go_qualification(self):
        """  
            进入职业证书页面
        """
        find_element(self.driver,self.qualification).click()

    def go_examination(self):
        """  
            进入考公考编页面
        """
        find_element(self.driver,self.examination).click()

    def go_Entrance_examination(self):
        """  
            进入升学考试页面
        """
        find_element(self.driver,self.Entrance_examination).click()

    def go_Entrepreneurship(self):
        """ 
            进入求职创业页面
        """
        find_element(self.driver,self.Entrepreneurship).click()