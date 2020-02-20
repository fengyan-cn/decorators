from sys import stdout

list1 = []
for i in range(10):
    list1.append([])
    for j in range(10):
        list1[i].append(0)

for i in range(10):
    list1[i][0] = 1
    list1[i][i] = 1

for i in range(2, 10):
    for j in range(1, i):
        list1[i][j] = list1[i-1][j-1] + list1[i-1][j]

for i in range(10):
    for j in range(i+1):
        stdout.write(str(list1[i][j]))
        print('\t', end='')
    print()