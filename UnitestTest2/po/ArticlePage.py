from utils.seleniumtools import find_element

class ArticlePage():
    """  
        文章页面
    """
    def __init__(self, driver):
        self.driver = driver
        self.title = "测评网-写文章"
        self.url = "http://193.112.79.96:8080/ljindex/html/experience_new.html"
        self.user_article_title = ("id", 'user_article_title')
        self.content = ("id", 'text-elem04355473107167662')
        self.ximg = ("name", 'file')
        self.brief = ("id", 'user_article_breif')
        self.new_tags = ("id", 'new_tags')
        self.new_tag = ("id", 'new_tag')
        self.tagbutton = ("class name", 'btn btn-danger')
        self.tag0 = ("id", 'tag0')
        self.questioncommit = ("id", 'allcommit')


    def question(self, title, content, ximg, pwd, brief, new_tag):
        """ 
        添加问题代码
        """
        find_element(self.driver, self.title).send_keys(title)      # 标题
        find_element(self.driver, self.content).send_keys(content)  # 内容
        find_element(self.driver, self.ximg).send_keys(ximg)        # t图片
        find_element(self.driver, self.brief).send_keys(brief)      # 介绍
        find_element(self.driver, self.new_tags).click()            # 点击新建标签
        find_element(self.driver, self.new_tag).send_keys(new_tag)     # 输入标签
        find_element(self.driver, self.tagbutton).click()           # 提交标签
        find_element(self.driver, self.tag0).click()                # 点击选中输入的标签
        find_element(self.driver, self.questioncommit).click()      # 点击问题提交
