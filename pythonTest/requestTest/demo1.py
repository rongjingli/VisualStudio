import requests

""" url ="http://192.144.148.91:2333/get_title_img?num=3"

res = requests.get(url)
print(res.text) 

"""

#登陆
url ="http://192.144.148.91:2333/login"
parameter ={"username":"tunan","password":"asd123456"}
res = requests.post(url =url, json=parameter)
print(res.text)
token =res.json()["data"]["token"]


#评论
url2 ="http://192.144.148.91:2333/comment/new"
parameter1 ={"ctype": 1, "comment": "奥克兰技术的flak即使对方", "fid": "3797"}
h1token={"token":token}
res = requests.post(url =url2, json=parameter1, headers=h1token)
print(res.text)