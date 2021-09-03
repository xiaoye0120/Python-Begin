# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/21  17:28

the_count=[1,2,3,4,5]
fruits=['apples','oranges','pears''apricots']
change=[1,'pennies',2,'dimes','3','quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d"%number)

#same as above
for fruits in fruits:
    print("A fruits of type:%s"%fruits)

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r"%i)

#we can also build lists,first start with an empty one
elements=[]

#then use the range function to do 0 to 5 counts
for i in range(0,6):
    print("Adding %d to the list."%i)
    #append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print("Element was :%d"%i)

"""
1. cmp(list1,list2)
比较两个列表的元素
2.len(list)
列表元素个数
3.max(list)
返回列表元素最大值
4.min(list)
返回列表元素最小值
5.list(seq)
将元组转换为列表
"""

"""
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort(cmp=None, key=None, reverse=False)
对原列表进行排序
"""
