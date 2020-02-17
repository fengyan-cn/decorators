from functools import reduce
list1 = []
pause = 0
num = int(input('想重复几次呢:'))
a = int(input('基础数字'))
for i in range(num):
    pause = pause + a
    a = a * 10
    list1.append(pause)
Sum = reduce(lambda x,y: x + y,list1)
print(Sum)