import unittest,requests 
import os, sys
sys.path.append(os.getcwd())
from utils.geturlParams import geturlParams


@unittest.skip("屏蔽类")
class TestCasesSelect(unittest.TestCase):

    def setUp(self):
        # geturlParams().get_Url()
        self.base_url = geturlParams().get_Url()

    def tearDown(self):
        print(self.result)

    def test_01_showversion(self):
        """ 查看版本号接口 """
        res = requests.get(self.base_url+"/showversion")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '查询成功')

    def test_03_getcoures(self):
        """ 获取首页轮播图 """
        res = requests.get(self.base_url+"/getcoures?pagenum=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')
        
    def test_04_coure(self):
        """ 获取教程详情 """
        res = requests.get(self.base_url+"/get/coure?cid=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_05_getquestions(self):
        """ 获取热门讨论 """
        res = requests.get(self.base_url+"/getquestions?pagenum=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_06_question(self):
        """ 获取问题详情 """
        res = requests.get(self.base_url+"/get/question?qid=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_07_getarticle(self):
        """ 获取热门文章 """
        res = requests.get(self.base_url+"/getarticle?pagenum=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_08_article(self):
        """ 获取文章详情 """
        res = requests.get(self.base_url+"/get/article?aid=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_09_getinspirer(self):
        """ 获取灵感 """
        res = requests.get(self.base_url+"/getinspirer?pagenum=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')
    def test_10_inspirer(self):
        """ 获取灵感详情 """
        res = requests.get(self.base_url+"/get/inspirer?iid=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_11_gethighusers(self):
        """获取活跃用户 """
        res = requests.get(self.base_url+"/gethighusers?num=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_12_getcomments(self):
        """post请求 获取评论列表 """
        d = {"ctype": 0, "fid":"1", "pagenum":"1"}
        res = requests.post(self.base_url+"/getcomments", json=d)
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_14_getmblist(self):
        """获取密保问题列表 """
        res = requests.get(self.base_url+"/getmblist")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_15_gettaglist(self):
        """获取标签列表 """
        res = requests.get(self.base_url+"/gettaglist?type=0")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_16_search(self):
        """搜索 """
        res = requests.get(self.base_url+"/search?type=0&value=张三&pagenum=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_17_getuserinfo(self):
        """获取用户详情 """
        res = requests.get(self.base_url+"/get/userinfo?uid=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_18_userinspirer(self):
        """获取用户的灵感列表 """
        res = requests.get(self.base_url+"/userinspirer?uid=251&pagenum=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_19_userarticle(self):
        """获取用户文章列表 """
        res = requests.get(self.base_url+"/userarticle?uid=251&pagenum=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_20_userquestions(self):
        """获取用户问题列表 """
        res = requests.get(self.base_url+"/userquestions?uid=251&pagenum=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_21_getuserfollows(self):
        """获取用户关注人列表"""
        res = requests.get(self.base_url+"/getuserfollows?uid=251")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_22_getuserfens(self):
        """获取用户粉丝列表 """
        res = requests.get(self.base_url+"/getuserfens?uid=251")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')

    def test_23_getuserdt(self):
        """获取用户动态列表 """
        res = requests.get(self.base_url+"/getuserdt?uid=251&pagenum=1")
        self.result = res.json()
        assert res.status_code ==200
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['msg'], '操作成功！')
