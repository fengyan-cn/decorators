from functools import reduce
a = 2
b = 1
Sum = 0
list1 = []
for i in range(20):
    list1.append(a/b)
    b, a = a, a+b
Sum = reduce(lambda x,y:x+y,list1)

if len(list1) == 20:
    print('序列是对的,总和是:',Sum)