# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/18  20:43

from sys import argv

script,filename=argv

print("We're going to erase %r."%filename)

input(">")

print("Opening the file...")

#打开目标文件，并写入操作
target=open(filename,'w')

print("Truncating the file.Goodbye")

#清楚文件内容
target.truncate()

print("Now I'm going to ask you for three lines.")

line1=input("line1:")
line2=input("line2:")
line3=input("line3:")

print("I'm going to write these to the file.")



#用一行代码代替三个输入
target.write(f'{line1}\n{line2}\n{line3}\n')
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#arget.write("\n")

print("And finally,we close it.")
#关闭文件
target.close()