list1 = []
list2 = []
for i in range(3):
    list1.append([])
    list2.append([])
    for j in range(3):
        list1[i].append(int(input('列表1请输入一个数')))
        list2[i].append(int(input('列表2请输入一个数')))

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(list1)):
    for j in range(len(list1[0])):
        result[i][j] = list1[i][j] + list2[i][j]  # 出现了一个很有意思的情况，如果7、8行不加int就是字符串，那么+号会直接把两边连起来
print(list1)
print(list2)
print(result)

