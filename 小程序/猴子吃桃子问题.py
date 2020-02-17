x2 = 1
#逆推思想
for i in range(9, 0, -1):
    x1 = (x2+1) * 2
    x2 = x1

print(x1)
