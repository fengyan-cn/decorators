import random

list1 = [x for x in range(1, 51)]

for i in range(7):
    a = random.choice(list1)
    print('被选中的数字就是:', a)
    print(a * '*')