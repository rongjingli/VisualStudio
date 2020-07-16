from utils.readConfig import ReadConfig
 
class geturlParams():# 定义一个方法，将从配置文件中读取的进行拼接
    
    def get_Url(self):
        readconfig = ReadConfig()
        scheme= readconfig.get_http('scheme')
        url = readconfig.get_http('baseurl')
        port = readconfig.get_http('port')
        new_url = scheme+'://' + url + ':'+ port
        # logger.info('new_url'+new_url)
        return new_url
 
if __name__ == '__main__':# 验证拼接后的正确性
    print(geturlParams().get_Url())