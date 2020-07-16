import time, unittest
import requests
from utils.dbtools import chaxun



# 显示等待必须加这个
# from selenium.webdriver.support.ui import WebDriverWait

# 类的继承
@unittest.skip("不要想让他执行")
class TestCassindex(unittest.TestCase):

    def setUp(self):
        print("接口测试开始")
        self.URL="http://193.112.79.96:2333"
    def tearDown(self):
        print("接口测试结束!")
    # 查询版本
    def test_01_showversion(self):
        url= self.URL+"/showversion"
        res=requests.get(url)
        assert res.status_code==200 and res.json()["status"]==200
    # 获取首页轮播图
    def test_02_get_title_img(self):
        url= self.URL+"/get_title_img"
        res=requests.get(url)
        assert res.status_code==200 and res.json()["status"]==200

        id=res.json()["data"][0]["id"]
        sql="select * from t_title_img where id={}".format(id)
        assert len(chaxun(sql))!=0
    # 获取推荐教程
    def test_02_get_title_img(self):
        # 参数页码 一页最多10条数据,如果不传，默认返回3条
        pagenum1=1
        url= self.URL+"/getcoures?pagenum="+pagenum1
        res=requests.get(url)
        assert res.status_code==200 and res.json()["status"]==200

        id=res.json()["data"]["contentlist"][0]["id"]
        sql="select * from t_coures where id={}".format(id)
        assert len(chaxun(sql))!=0


