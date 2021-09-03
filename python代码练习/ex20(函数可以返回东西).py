# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/19  22:43

def add(a,b):
    print("ADDING %d+%d"%(a,b))
    return a+b

def subtract(a,b):
    print("SUBTRACTING %d-%d"%(a,b))
    return a-b

def multiply(a,b):
    print("MUlTIPLYING %d*%d"%(a,b))
    return a*b

def divide(a,b):
    print("DIVIDING %d/%d"%(a,b))
    return a/b

print("Let's do some math with just functions!")

age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print("Age:%d,Height:%d,Weight:%d,IQ:%d"%(age,height,weight,iq))

print("Here is a puzzle.")

what=add(age,subtract(height,multiply(weight,divide(iq,2))))
#That=age+(height-(weight*(iq/2)))
print("That becomes:",what,"Can you do it by hand?")


