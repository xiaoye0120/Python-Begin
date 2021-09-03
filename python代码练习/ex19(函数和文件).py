# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/19  22:20

from sys import argv

script,input_file=argv
#定义函数：打印读取的文件
def print_all(f):
    print(f.read())
#定义函数：调整读写位置到开头
def rewind(f):
    f.seek(0)
#定义函数：打印第一个参数，同时打印该文件磁头所在的一行
def print_a_line(line_count,f):
    print(line_count,f.readline())
#打开文件
current_file=open(input_file)

print("First let's print the whole file:\n")
#打印整个文件
print_all(current_file)

print("Now let's rewind,kind of like a tape.")
#调用函数，将读写位置放到开头
rewind(current_file)

print("Let't print three lines:")

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)