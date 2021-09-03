# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/24  14:54
#创建一个新的空列表
numbers = []
#定义循环函数
def whileloop(n,a):
    i = 0
    while i<n:
     print("At the top i is %d"%i)
     numbers.append(i)
     i=i+a
     print("Numbers now:",numbers)
     print("At the bottom i is %d"%i)

a=int(input("a="))
n=int(input("n="))
whileloop(n,a)
print("The numbers:")

#遍历列表
for num in numbers:
    print(num)