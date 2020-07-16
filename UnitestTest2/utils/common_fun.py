import csv
import time

import os

from baseView.baseView import BaseView

# 封装的是通用类 继承BaseView 所以他也有查找元素 以及初始化的函数
from common.selenium_driver import logutil, getBaseUrl


class Common(BaseView):
    # 获取当前格式化的时间
    def getTime(self):
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now

    # 封装获取截图的函数
    def getScreenShot(self, module):
        time = self.getTime()
        # 截图文件的命名位置及方式,放在screenshots文件夹下面,以模块名字及时间命名
        # os.path.dirname(__file__)得到当前文件所在的文件夹 os.path.dirname(common)拿到common所在的文件夹
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logutil.info('获取截图 %s screenshot' % module)
        # 得到截图
        self.driver.get_screenshot_as_file(image_file)

    # 封装读取excel表格数据的函数 传入csv文件的路径
    def get_csv_data(self, csv_file, line):
        logutil.info('=====获取csv的数据======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            # 读取csv文件
            reader = csv.reader(file)
            # 让他默认索引从1开始 在传入的时候从1开始传 不是0
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    # 封装打开首页
    def openMainPage(self):
        self.driver.get(getBaseUrl()+'/shop/index')