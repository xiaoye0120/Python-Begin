# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/25  20:53

class TheThing(object): #类的声明，object不能省略

    def __init__(self): #这里是in it的意思，即设置内部变量
      self.number=0

    def some_function(self):#class中的固定的参数，实现变量x，函数名y（self）的用法中函数的参数即为x
        print("I got called.")

    def add_me_up(self,more):
        self.number+=more
        return self.number

#two different things
a=TheThing()#定义变量a为TheThing类，以下相同
b=TheThing()

a.some_function() #对a调用TheThing类里的some_function函数，以下相同
b.some_function()

print(a.add_me_up(20))  #对a调用TheThing类里的add_me_up函数，以下相同
print(a.add_me_up(20))
print(b.add_me_up(30))
print(b.add_me_up(30))

print(a.number) #打印当前a.number的值，由于类中self.number=0,所以定义a为TheThing类时，该值为零
print(b.number)