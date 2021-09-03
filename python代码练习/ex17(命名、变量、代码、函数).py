# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/19  17:06

#输出两个值函数
def print_two(*args):
    arg1,arg2=args
    print("arg1:%r,arg2:%r"%(arg1,arg2))


def print_two_again(arg1,arg2):
    print("arg1:%r,arg2:%r"%(arg1,arg2))

def print_one(arg1):
    print("arg1:%r"%arg1)

def print_none():
    print("I got nothing")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
