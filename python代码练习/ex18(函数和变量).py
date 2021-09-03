# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/19  22:05

#定义函数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print("You have %d cheeses!"%cheese_count)
    print("You have %d boxes of crackers!"%boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#打印语句，传递两个数给函数
print("We can just give the function numebers directly:")
cheese_and_crackers(20,30)

#打印语句，定义两个变量
print("Or,we can use variables from our script:")
amount_of_cheese=10
amount_of_crackers=50
#将定义的变量传递到函数中
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#打印语句，传递数值的计算式给函数
print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)

#打印语句，传递变量和数值的计算式给函数
print("And we can combine the two,variables and math:")
cheese_and_crackers(amount_of_cheese+100,
amount_of_crackers+1000)