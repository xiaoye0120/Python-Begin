# 努力学习编程的小垃圾
# 不好好学就是废物
# 学习时间：2021/8/25  14:02

cities={'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}

cities['Ny']='New York'
cities['OR']='Portland'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not found"

#pay attention!
cities['_find']=find_city

while True:
    print('State?(ENTER to quit)'),
    state=input(">")
    if not state:break

    #this line is the most important ever! study!
    city_found=cities['_find'](cities,state)
    print(city_found)