def save(driver):
    with open("cookie.txt", "w") as f:
        cookie =str(driver.get_cookies()[0])
        # 只能存字符串,不能存字典 失败
        f.writelines(cookie)
        

def read():
    with open("cookie.txt", "r") as f:
        cookie = f.read()
    return cookie