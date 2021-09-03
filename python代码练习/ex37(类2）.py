# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/25  21:30

class Test(object):
    a = 10

    def __init__(self):
        pass
    def test_getattr(self):
        self.d=10
        b = 20
        return self.d

if __name__ == '__main__':
    t = Test()

    result_1 = getattr(t,'test_getattr','NO_Method') # 获取对象t中的'test_getattr'的方法，存在就打印出方法的内存地址。
    result_2 = getattr(t,'a','default') # 获取对象t中的a变量，若没有，则返回default
    result_3 = getattr(t,'c','default') # 获取对象t中的c变量，若没有，则返回default
    result_4 = getattr(t,'test_getattr')() # 获取对象t中的test_getattr方法，后面加括号可以将这个方法运行。

    print('result_1=', result_1)
    print('result_2=', result_2)
    print('result_3=', result_3)
    print('result_4=', result_4)
