# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/18  21:09

from sys import argv
from os.path import exists

script,from_file,to_file=argv

print("Copying from %s to %s"%(from_file,to_file))
#打开文件进行读取文件内容
indata=open(from_file).read()

print("The input file is %d bytes long"%len(indata))

print("Does the output file exist?%r"%exists(to_file))

#写入文件内容
output=open(to_file,"w")
output.write(indata)

print("Alright,all done.")

output.close()
