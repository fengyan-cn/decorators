from math import sqrt
from sys import stdout

prime = []
for num in range(101,201):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)