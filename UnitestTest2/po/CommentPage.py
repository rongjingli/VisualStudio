from utils.seleniumtools import find_element

class CommentPage():
    """     
       评论页面
    """
    def __init__(self, driver):

        self.driver = driver
        self.comment1 = ("id", 'question_comments_ctt')
        self.comment_btn = ("id", 'question_comments_btn')


    def comment(self,  comment):
        """ 
        添加;评论
        """
        find_element(self.driver, self.comment1).send_keys(comment)  # 内容
        find_element(self.driver, self.getinspirercommit).click()      # 点击提交
