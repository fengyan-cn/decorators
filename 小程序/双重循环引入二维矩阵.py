list1 = []
Sum = 0
for i in range(3):
    list1.append([])
    for j in range(3):
        list1[i].append(input('随便你加什么只要是数字就行'))

for i in range(3):
    Sum += int(list1[i][i])

print(list1)
print(Sum)