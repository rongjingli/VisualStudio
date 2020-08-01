import unittest
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import send_email

# 1,加载所用的测试用例
# unittest自动到case文件夹下去查找test_*.py的里面的所用继承untest.testCase的test_方法.
testcase = unittest.defaultTestLoader.discover("case","test_*.py")

# 2,使用htmltestrunner运行测试用例,并收集测试报告
filepath="./report/report.html"
title='测试报告'
desc="这个测试报告描述"
# wb w=写 b=字节  以字节的方式写入它 as f 用一个f的变量保存起来
with open(filepath,"wb") as f:
    runner=HTMLTestRunner(stream=f,title=title,description=desc)
    runner.run(testcase)



# 3.发送邮件，发送最新测试报告html
send_email(filepath)