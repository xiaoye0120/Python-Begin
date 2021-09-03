# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/11  21:11
#从sys导入argv模块来使用参数
from sys import argv

#使用两个参数，脚本名称和文件名称
script,filename=argv
#获取文件名
txt=open(filename)

#打印文件名称
print("Here's your file %r:"%filename)
#打印文件内容
print(txt.read())

#打印重新输入文件名的信息
print("Type the filename again:")

#输入提示符
file_again=input("> ")

#打开重新输入的文件名的文件并存入变量
txt_again=open(file_again)

#打印重新输入文件的内容
print(txt_again.read())