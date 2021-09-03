# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/10  17:20
cars= 100  #车的数量
space_in_a_car=4  #车的容量
drivers=30  #驾驶员
passengers=90 #乘客
cars_not_driven=cars-drivers  #空闲车辆
cars_driven=drivers    #工作车辆
carpool_capacity=cars_driven+space_in_a_car  #车的总容量
average_passengers_per_car=passengers/cars_driven      #平均乘客数


print("There are",cars,"cars available")
print("There are only",drivers,"drivers available")
print("There will be",cars_not_driven,"empty cars today")
print("We can transport",carpool_capacity,"people today")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car")