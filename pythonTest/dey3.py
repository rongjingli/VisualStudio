

class Person():

    name ="张三"
    sex ="男"
    age =18

    def talk(self):
        print("可以说话")

    def eat(self, parameter):
        print("开溜开溜,{}".format(parameter))
        return "自由女神"

p=  Person()

a = p.eat("荣敬")
print(a)