# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:整合自动发邮件功能，执行测试用例生成最新测试报告，取最新的测试报告，发送最新测试报告
问题，邮件始终不能显示html：将电脑时间改为北京时间即可
'''
import unittest

import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


# 3.定义：发送邮件，发送最新测试报告html
def send_email(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    mail_body = f.read()
    # 调试使用
    #    print u'打印'
    #    print mail_body
    # 关闭文件
    f.close()
    #邮箱15330276178@163.com  密码zhiyuan0932
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名/密码 ----设置自己邮箱变成服务邮箱--需要设置
    user = 'rongjing1037@163.com'
    # 邮箱授权码
    password = 'YMLCGXYUIDGURHOT'
    # 发送邮箱
    sender = 'rongjing1037@163.com'
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = ['jing1037118812@163.com']
    # 发送邮件主题
    subject = '自动定时'+ str(time.strftime('%Y%m%d%H%M%S'))+'发送测试报告'

    # 编写 HTML类型的邮件正文
    # MIMEText这个效果和下方用MIMEMultipart效果是一致的，已通过。
    #    msg = MIMEText(mail_body,'html','utf-8')

    msg = MIMEMultipart('mixed')

    # 注意：由于msg_html在msg_plain后面，所以msg_html以附件的形式出现
    #    text = "Dear all!\nThe attachment is new testreport.\nPlease check it."
    # 中文测试ok
    #    text = "Dear all!\n附件是最新的测试报告。\n麻烦下载下来看，用火狐浏览器打开查看。\n请知悉，谢谢。"
    #    msg_plain = MIMEText(text,'plain', 'utf-8')
    #    msg.attach(msg_plain)

    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)

    # 以附件的方式发送：但是会报554，倍163退信。--此路不通。
    #    msg_html = MIMEText(mail_body,'base64','utf-8')
    #    msg_html["Content-Type"] = 'application/octet-stream'
    #    msg_html.add_header('Content-Disposition', 'attachment', filename='testreport.html')
    #    msg.attach(msg_html)

    # 要加上msg['From']这句话，否则会报554的错误。
    # 要在163有限设置授权码（即客户端的密码），否则会报535
    msg['From'] = 'rongjing1037@163.com <rongjing1037@163.com>'
    #    msg['To'] = 'XXX@doov.com.cn'
    # 多个收件人
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

# if __name__ == '__main__':
#     print
#     '=====AutoTest Start======'
#     # 测试报告的地址
#     test_report_dir = 'E:\\VisualStudio\\UnitestTest2\\report\\report.html'
    
#     # 2.取最新测试报告
#     new_report = new_file(test_report_dir)
#     # 调试用的测试报告的地址
#     #    print new_report

#     # 3.发送邮件，发送最新测试报告html
#     send_email(new_report)
#     print
#     '=====AutoTest Over======'
