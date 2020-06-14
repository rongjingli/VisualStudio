def save(res):
    with open("token.txt","w")as f:
        token=res.json()["data"]["token"]
        f.writelines(token)

def read():
    with open("token.txt","r")as f:
        token= f.read()
    return token